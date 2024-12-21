/* unsigned int discarded_wagons (Train t, unsigned int size){

  unsigned int discart_wagons = 0u; 
  unsigned int j = 0u; 
  unsigned int i = 0u; 

  while(i<size-2u){
    if(t[i].cargo == oatmeal && t[i+1].cargo == oatmeal && t[i+2].cargo == oatmeal){
      j = i+2; 
      while(j < size && t[j].cargo == oatmeal){
        discart_wagons += 1; 
        j++;
      }
      i = j; 
    }
    else{
      i++;
    }
  }
  return discart_wagons;
}

  
  for(unsigned int i = 0u; i<size-2u; i++){
    if(t[i].cargo == oatmeal && t[i+1].cargo == oatmeal && t[i+2].cargo == oatmeal){
      j = i+2; 
      while(j < size && t[j].cargo == oatmeal){
        res += 1; 
        j++;
      }
    }
 
  for(unsigned int i = 0u; i<size-1u; i++){
    if(t[i].cargo == oatmeal && t[i+1].cargo == oatmeal){

    }
  }


  for(unsigned int i = 0u; i<size-1u; i++){
    if(t[i].cargo == oatmeal){
      while(i<size){

      }
    }
    else{
      skip;
    }
  }
    while()

    if i == 2 
 
 unsigned int j = 0u;
  unsigned int groups = 0u;

  for(unsigned int i = 0u; i<size; i++){
    j = i; 
    while(t[j].cargo==oatmeal && j<size-1u){
      j++;
    }
    if(j>2){
      groups += j; 
    }
  }

  res = groups - 

  return groups;  

    unsigned int j = 0u;
  unsigned int groups = 0u;

  while(i<size){
    j = i; 
    while(t[j].cargo==oatmeal && j<size-1u){
      j++;
    }
    if(j>2){
      groups += j; 
    }
  }

  res = groups - 

  return groups; 

    unsigned int res = 0u; 
  unsigned int j = 0u; 

  for(unsigned int i = 0u; i<size-2u; i++){
  while(i<size-2u){
    if(t[i].cargo == oatmeal && t[i+1].cargo == oatmeal && t[i+2].cargo == oatmeal){
      j = i+2; 
      while(j < size && t[j].cargo == oatmeal){
        res += 1; 
      }
      i = j; 
    }
    i++;
  }  

*/