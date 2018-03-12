def copy(node1, node2):
    """ 
    Copies all of the expressions, keyframes, and values from the parameters of node 1 (first selected node) 
    to the parameters of node 2 (second selected node), if a parameter with the same name is found.
    """
    
    
    # ITERATE OVER ALL PARMS IN NODE1, AND CHECK IF THE PARM EXISTS IN NODE2
    for p in node1.parms():
        if node2.parm(p.name()):
            p2 = node2.parm(p.name())
            
            # TEMPORARILY CLEAR KEYFRAMES. WE WILL RESTORE THEM LATER IF THEY EXIST ON NODE1'S PARM
            p2.deleteAllKeyframes()
            
            # SEE IF WE CAN JUST SET THE EXPRESSION OF THE PARAMETER
            try:
                p2.setExpression(p.expression())
            except:
                # IF NOT, TRY SETTING THE UNEXPANDED STRING. IF THAT DOESN'T WORK, JUST SET THE EVAL VALUE OF THE PARM
                try:
                    p2.set(p.unexpandedString())
                except:
                    p2.set(p.eval())
                    
            # SET KEYFRAMES IF THEY EXIST ON NODE1
            if p.keyframes():
                p2.setKeyframes(p.keyframes())

# CHECKS SELECTED NODE AND SENDS TO COPY FUNCTION                
def run():
    """
    Gets the currently selected nodes and runs the copy function.
    """
    
    # GET SELECTED NODES
    sel = hou.selectedNodes()
    
    # DISPLAY WARNINGS IF TWO NODES ARE NOT SELECTED
    if len(sel) < 2:
        hou.ui.displayMessage("Please select two nodes.")
    if len(sel) > 2:
        hou.ui.displayMessage("Please only select two nodes.")

    # INITIALIZE VARIABLES
    node1 = sel[0]
    node2 = sel[1]
    missing_list = []
    different_list = []    
    checked_list = []

    # COPY PARAMETERS
    copy(node1, node2)

                
run()                    
