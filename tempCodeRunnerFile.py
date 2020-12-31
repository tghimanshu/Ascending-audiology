g == 'red_circle_nr'):   
        ex = check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_circle_nr, tags=arg+str(points_count[arg]))
        points[arg[:-3]].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_X_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_X_nr, tags=arg+str(points_count[arg]))
        points[arg[:-3]].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'red_open_bracket_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_open_bracket_nr, tags=arg+str(points_count[arg]))
        points[arg[:-3]].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_close_bracket_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_close_bracket_nr, tags=arg+str(points_count[arg]))
        points[arg[:-3]].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'red_sq_bkt_nr'):    
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_sq_bkt_nr, tags=arg+str(points_count[arg]))
        points[arg[:-3]].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_sq_bkt_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_sq_bkt_nr, tags=arg+str(points_count[arg]))
        points[arg[:-3]].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        cre