#include "big_brother.h"
#include "fat_volume.h"
#include "fat_table.h"
#include "fat_util.h"
#include "fat_file.h"
#include <stdio.h>
#include <string.h>

int bb_is_log_file_dentry(fat_dir_entry dir_entry) {
    return strncmp(LOG_FILE_BASENAME, (char *)(dir_entry->base_name), 3) == 0 &&
           strncmp(LOG_FILE_EXTENSION, (char *)(dir_entry->extension), 3) == 0;
}

int bb_is_log_filepath(char *filepath) {
    return strncmp(BB_LOG_FILE, filepath, 8) == 0;
}

int bb_is_log_dirpath(char *filepath) {
    return strncmp(BB_DIRNAME, filepath, 15) == 0;
}

/* Searches for a cluster that could correspond to the bb directory and returns
 * its index. If the cluster is not found, returns 0.*/
u32 search_bb_orphan_dir_cluster() {
    /*Debo recorrer la fat table hasta encontrar el primer cluster que cumpla con los requisitos 
    Su entrada en la tabla FAT está marcada como Bad or reserved 0x0FFFFFF7.
    Su primera entrada de directorio es un archivo con nombre fs.log
    */
    u32 bb_dir_start_cluster = 0;
    int k10 = 10240;
    u8 *buf =NULL; 
    fat_volume vol = get_fat_volume(); 
    fat_table table= vol->table; 
    
    //Recorro la fat table para encontrar el cluster buscado 
    while(bb_dir_start_cluster < k10 ) { 
    
        u32 bytes_per_cluster = fat_table_bytes_per_cluster(table); //Calculo cantidad de bytes por cluster 

        off_t offset = fat_table_cluster_offset(table, bb_dir_start_cluster); //Obtengo dirección en disco del cluster

        buf = alloca(bytes_per_cluster); //Pido memoria para el bufer

        full_pread(table->fd, buf, bytes_per_cluster, offset); //Leo los datos de la primer dir_entry y lo guardo en buf 

        int is_log_file = bb_is_log_file_dentry((fat_dir_entry) buf); //Chequeo si la dir_entry corresponde al archivo fs.log

        if(fat_table_cluster_is_bad_sector(bb_dir_start_cluster) && (is_log_file==0)){
            break; //Termina el ciclo. Encontré el cluster.
        }
        else {
            bb_dir_start_cluster++;
        }
        
    }

    return bb_dir_start_cluster;
}



/* Creates the /bb directory as an orphan and adds it to the file tree as 
 * child of root dir.
 */
int bb_create_new_orphan_dir() {

    fat_volume vol = get_fat_volume(); 
    fat_tree tree = vol->file_tree; 
    fat_tree_node root_node = NULL;
    int k10 = 10240;
    u32 cluster = search_bb_orphan_dir_cluster(); 
    errno = 0;

    if (cluster>=k10){  //No encontró el directorio
        //Si el directorio no existe, crear el directorio y el archivo de logs dentro del directorio, que lo llamaremos bb (definido por BB_DIRNAME).
        u32 free_cluster = fat_table_get_next_free_cluster(vol->table); //Busco el primer cluster free
    
        // Create a new file from scratch, instead of using a direntry like normally done.
        fat_file loaded_bb_dir = fat_file_init_orphan_dir(BB_DIRNAME, vol->table, free_cluster);

        // Add directory to file tree. It's entries will be like any other dir.
        root_node = fat_tree_node_search(vol->file_tree, "/");

        //Agrego el directorio al árbol
        vol->file_tree = fat_tree_insert(vol->file_tree, root_node, loaded_bb_dir);

        fat_file parent = fat_tree_get_file(root_node);
        fat_file_dentry_add_child(parent,loaded_bb_dir); 
    
        
    }
    else{ //Existe el directorio.En tal caso, ya está creado el fs.log 
    
        // ****MOST IMPORTANT PART, DO NOT SAVE DIR ENTRY TO PARENT ****
        
        // Create a new file from scratch, instead of using a direntry like normally done.
        fat_file loaded_bb_dir = fat_file_init_orphan_dir(BB_DIRNAME, vol->table, cluster);

        // Add directory to file tree. It's entries will be like any other dir.
        root_node = fat_tree_node_search(vol->file_tree, "/");
        vol->file_tree = fat_tree_insert(vol->file_tree, root_node, loaded_bb_dir);

        //Busco el nodo del directorio huérfano
        fat_tree_node dir_node = fat_tree_node_search(tree,BB_DIRNAME); 

        //Leo los hijos del directorio
        GList* children= fat_file_read_children(loaded_bb_dir);
        
        //Agrego los hijos del directorio en el árbol
        if (children!=NULL){
            for (GList* list = children; list != NULL ;list= list->next){
                 vol->file_tree = fat_tree_insert(tree,dir_node,(fat_file)list->data); //Agrego el archivo de logs al árbol     
            }     
        }
        
    }
    
    return -errno;
 }

