#include <stdio.h>
#include <unistd.h> /* Para funciones gethostname y getcwd */
#include <pwd.h>    /* Para getpwuid */

#include "prompt.h"

void show_prompt(void) {
    char host_name[256];
    host_name[255] = '\0'; 
    gethostname(host_name, 256); //Obtengo el nombre del host

    unsigned int user_id = geteuid();
    struct passwd* user_password = getpwuid(user_id); //Obtendré el nombre de usuario accediendo a pw_name

    char relative_path[2556];
    relative_path[2555] = '\0';
    getcwd(relative_path,2556); //Obtengo el camino relativo
    
    printf("%s@%s" ":~/mybash>" "%s" "$ ",user_password->pw_name,host_name,relative_path);
    fflush (stdout);
}