
/*
    assert(!stack_is_empty(s));

    stack p=s; 
    while(p->next!=NULL){
        p = p->next; 
    }
    free(p);
    return s;


stack_elem stack_top(stack s){
    stack_elem e;
    stack p=s; 
    while(p->next!=NULL){
        p = p->next;
    }
    e = p->elem; 
    return e; 
}

  stack s; 
  s = stack_empty();
  for (unsigned int i = 0u; i<length; i++){  
    s = stack_push(s, array[i]);
  }
  new_array = malloc(sizeof(int) * length);   
  for (unsigned int i = 0u; i<length; i++){
    new_array[i] = stack_top(s);
    s = stack_pop(s);
  }

    /*stack_elem *array[n]; 
  */
 
 