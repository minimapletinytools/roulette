import time
import random #use random.choice(list) to get random elt from list
#TODO this is broekn with multiple clip managers. need to give each one an id
def getTimeOnFrame(state):
    return time.time()-state["time_enter_frame"]
def getSubset(aset,idlist):
    #make sure idlist is a LIST not a string
    #todo make sure this does not return one element twice
    s = list()
    for e in idlist:
        for f in aset:
            if e in f[0]:
                s.append(f)
    return s
    
def removeElementFromSet(aset,elt):
    for e in aset:
        if e[1] == elt:
            aset.remove(e)
            break
def saveMemory(state,frame):
    if "MEMORY" in state:
        del state["MEMORY"]
    memory = (dict(state),frame)
    state["MEMORY"] = memory
    print "memory saved", memory
    
def loadMemory(state):
    if "MEMORY" in state:
        memory = state["MEMORY"]
    else:   #this case should not happen
        print "resetting game"
        state["RESET"] = 0
        return "-1"
    return memory

def init_graph(state):
    state["time_enter_frame"] = time.time()
    state["first_shot"] = True
    state["first_hesitate"] = True
    state["eyes_open"] = True
    #(category, name)
    state["visited"] = list([
                        ("FH1",u"FH1_1"),
                        ("FH1",u"FH1_2"),
                        ("FH1",u"FH1_3"),
                        (("FS","FH2"),u"FH2_1"),    #this is kind of backwards, but we want to pick this and NOT fs
                        ("FH2",u"FSFH2_2"),
                        ("FH2",u"FSFH2_3"),
                        ("FH3",u"FH3_1"),
                        ("FH3",u"FH3_2"),
                        ("FH3",u"FH3_3"),
                        ("FY",u"FY_1"),
                        ("FY",u"FY_2"),
                        ("FY",u"FY_3"),
                        ("DH",u"DH_1"),
                        ("DH",u"DH_2"),
                        ("DH",u"DH_3"),
                        ("YT",u"YT_1"),
                        ("YT",u"YT_2"),
                        ("YT",u"YT_3"),
                        ("SH1",u"SH1_1"),
                        ("SH1",u"SH1_2"),
                        ("SH1",u"SH1_3"),
                        ("lucky",u"lucky_1"),
                        ("lucky",u"lucky_2"),
                        ("lucky",u"lucky_3"),
                        ])
    
def on_new_frame(state):
    state["time_enter_frame"] = time.time()
    
def graph_default(state,clip):
    return -1
def graph_start(state,clip):
    if state["press"]:
        return "intro"
    else: return "-1"
def graph_wait(state,clip):
    if clip.getTimeLeft() < 0.2:
        state["blinking"] = True
    if state["lose"]:
        return "continue"
    if state["player_shoot_state"] == 2:
        state["player_shoot_state"] = 0
        return random.choice(getSubset(state["visited"],["lucky",]))[1]
    if clip.isFinished():
        if state["player_shoot_state"] == 0:
            if state["first_hesitate"]:
                if state["FH_state"] == 0:
                    return random.choice(getSubset(state["visited"],["FH1",]))[1]
                elif state["FH_state"] == 1:
                    if state["first_shot"]: return random.choice(getSubset(state["visited"],["FH2",]))[1]
                    else: return random.choice(getSubset(state["visited"],["FS",]))[1]
                elif state["FH_state"] == 2:
                    #alternatively, B decides to shoot self
                    return random.choice(getSubset(state["visited"],["FH3",]))[1]
            else:    #second hesitate
                return random.choice(getSubset(state["visited"],["SH1",]))[1]        
        return "wait"
    return "-1"

def graph_waitlean(state,clip):
    if clip.getTimeLeft() < 0.2:
        state["blinking"] = True
    if state["lose"]:
        return "continue"
    if state["player_shoot_state"] == 2:
        state["player_shoot_state"] = 0
        return random.choice(getSubset(state["visited"],["lucky",]))[1]
    if clip.isFinished():
        if state["player_shoot_state"] == 0 and getTimeOnFrame(state) > 1:
            if state["first_hesitate"]:
                #at this point B will shoot Y and Y can not do anything about it.
                state["first_hesitate"] = False
                state["turn"] = "B"
                return "FH4"
            else:
                state["turn"] = "B" 
                return "SH2"
    else: return "-1"
    
def graph_intro(state,clip):
    if clip.getTimeLeft() < 0.2:
        state["blinking"] = True
    if clip.isFinished():
        #we allow player to shoot himself now
        state["turn"] = "Y" 
        #TODO fix this
        saveMemory(state,"wait")
        return "wait"
    else: return "-1"
    
def FH_generic(state,clip,name):
    if clip.getTimeLeft() < 0.2:
        state["blinking"] = True
    if state["lose"]:
        return "continue"
    if clip.isFinished():
        #remove the element because we've been there already
        removeElementFromSet(state["visited"],name) 
        #advance state
        state["FH_state"] += 1
        return "wait"
    else: return "-1"
def FH3_generic(state,clip,name):
    if state["lose"]:
        return "continue"
    if clip.isFinished():
        #remove the element because we've been there already
        removeElementFromSet(state["visited"],name) 
        #advance state
        state["FH_state"] += 1
        return "waitlean"
    else: return "-1"
def graph_FH1_1(state,clip):
    return FH_generic(state,clip,"FH1_1")
def graph_FH1_2(state,clip):
    return FH_generic(state,clip,"FH1_2")
def graph_FH1_3(state,clip):
    return FH_generic(state,clip,"FH1_3")
def graph_FH2_1(state,clip):
    return FH_generic(state,clip,"FH2_1")
def graph_FSFH2_2(state,clip):
    state["first_shot"] = False
    return FH_generic(state,clip,"FSFH2_2")
def graph_FSFH2_3(state,clip):
    state["first_shot"] = False
    return FH_generic(state,clip,"FSFH2_3")
def graph_FH3_1(state,clip):
    return FH3_generic(state,clip,"FH3_1")
def graph_FH3_2(state,clip):
    return FH3_generic(state,clip,"FH3_2")
def graph_FH3_3(state,clip):
    return FH3_generic(state,clip,"FH3_3")
def graph_FH4(state,clip):
    if clip.isFinished(): return "BshootsY"
    else: return "-1"
def graph_Bgoesfirst(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"

def graph_BshootsY(state,clip):
    if clip.isFinished():
        state["shots_fired"] += 1
        if random.randint(0,5) <= state["shots_fired"]-1:
            return "continue" 
        else:
            if state["first_hesitate"]:
                return random.choice(getSubset(state["visited"],["FY",]))[1]
            else: return "BprepareshootB"   #need additional transition frame here
    else: return "-1"
def FY_generic(state,clip,name):
    if clip.isFinished():
        #remove the element because we've been there already
        removeElementFromSet(state["visited"],name) 
        #advance state
        return "BprepareshootB"
    else: return "-1"
def graph_FY_1(state,clip):
    return FY_generic(state,clip,"FY_1")
def graph_FY_2(state,clip):
    return FY_generic(state,clip,"FY_2")
def graph_FY_2(state,clip):
    return FY_generic(state,clip,"FY_3")

def graph_BprepareshootB(state,clip):
    if clip.isFinished(): 
        return random.choice(getSubset(state["visited"],["DH",]))[1]
    else: return "-1"
    
def DH_generic(state,clip,name):
    if clip.isFinished():
        #remove the element because we've been there already
        removeElementFromSet(state["visited"],name) 
        #advance state
        return "BshootsB"
    else: return "-1"
def graph_DH_1(state,clip):
    return DH_generic(state,clip,"DH_1")
def graph_DH_2(state,clip):
    return DH_generic(state,clip,"DH_2")
def graph_DH_3(state,clip):
    return DH_generic(state,clip,"DH_3")
def graph_BshootsB(state,clip):
    if clip.isFinished():
        state["shots_fired"] += 1
        if random.randint(0,5) <= state["shots_fired"]-1:
            return "Bdies"
        else:
            state["turn"] = "Y"
            return random.choice(getSubset(state["visited"],["YT",]))[1]
    else: return "-1"
def graph_Bdies(state,clip):
    if clip.isFinished(): return "youwin"
    else: return "-1"
def graph_youwin(state,clip):
    if clip.isFinished():
        state["RESET"] = 0
        return "-1"
    else: return "-1"

def YT_generic(state,clip,name):
    if clip.isFinished():
        #remove the element because we've been there already
        removeElementFromSet(state["visited"],name) 
        state["turn"] = "Y"
        saveMemory(state,"wait")
        return "wait"
    else: return "-1"
def graph_YT_1(state,clip):
    return YT_generic(state,clip,"YT_1")
def graph_YT_2(state,clip):
    return YT_generic(state,clip,"YT_2")
def graph_YT_3(state,clip):
    return YT_generic(state,clip,"YT_3")

def graph_continue(state,clip):
    if state["press"] and clip.getTime() > 1:
        state["press"] = False
        s,r =  loadMemory(state)
        if "MEMORY" in state:
            s["MEMORY"] = state["MEMORY"]
        #TODO state is not being assigned properly, need to do value by value
        state.clear()
        state.update(s)
        return r
    if clip.isFinished(): return "youlose"
    else: return "-1"
def graph_youlose(state,clip):
    if clip.isFinished():
        state["RESET"] = 0
        return "-1"
    else: return "-1"
    
def SH1_generic(state,clip,name):
    if state["lose"]:
        return "continue"
    if clip.isFinished():
        removeElementFromSet(state["visited"],name) 
        return "waitlean"
    else: return "-1"
def graph_SH1_1(state,clip):
    return SH1_generic(state,clip,"SH1_1")
def graph_SH1_2(state,clip):
    return SH1_generic(state,clip,"SH1_1")
def graph_SH1_3(state,clip):
    return SH1_generic(state,clip,"SH1_1")

def graph_SH2(state,clip):
    if clip.isFinished(): return "BshootsY"
    else: return "-1"
    
def lucky_generic(state,clip,name):
    if clip.isFinished():
        #remove the element because we've been there already
        removeElementFromSet(state["visited"],name) 
        return "BprepareshootB"
    else: return "-1"
def graph_lucky_1(state,clip):
    return lucky_generic(state,clip,"lucky_1")
def graph_lucky_2(state,clip):
    return lucky_generic(state,clip,"lucky_2")
def graph_lucky_3(state,clip):
    return lucky_generic(state,clip,"lucky_3")

    
    
#player functions
def graph_player_blank(state,clip):
    if state["turn"] == "Y":
        if state["player_shoot_state"] == 0 and state["press"]:
            state["player_shoot_state"] = 1
            return "player_handin"
        
    return "-1"
def graph_player_blank_patch(state,clip):
    print "blank!"
    if clip.getTime() > 0.5:
        state["eyes_open"] = False
    if not state["press"]:
        state["player_shoot_state"] = 0
        return "player_handout" 
    elif state["press"] and time.time() - state["time_pressed"] > 4:
        state["press"] = False
        print "KAPOW, Y shoots Y"
        state["turn"] = "B"
        #if random.randint(0,5) <= state["shots_fired"]-1:
        if 1:
            state["lose"] = True
            return "player_blank"
        else:
            state["player_shoot_state"] = 2
            #TODO clicky noise"
            return "player_handout"
    return "-1"
def graph_player_handin(state,clip):
    if clip.isFinished(): return "player_blank_patch"
    else: return "-1"
def graph_player_handout(state,clip):
    state["eyes_open"] = True
    if clip.isFinished(): return "player_blank"
    else: return "-1"
    
    
#eye functions
def graph_eyes_closing(state,clip):
    if state["lose"]:
        return "eyes_blank"
    if clip.isFinished() and state["eyes_open"]:
        return "eyes_openning" 
    else: return "-1"
def graph_eyes_openning(state,clip): 
    if clip.isFinished(): return "eyes_blank"
    else: return "-1"
def graph_eyes_blank(state,clip):
    #TODO fix bug here where you can not shoot when blinking
    if state["blinking"]:
        return "eyes_blink"
    if not state["eyes_open"]:
        return "eyes_closing"
    return "-1"
def graph_eyes_blink(state,clip):
    if clip.isFinished():
        state["blinking"] = False 
        return "eyes_blank"
    else: return "-1"
