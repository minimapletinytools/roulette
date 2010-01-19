import time
import random #use random.choice(list) to get random elt from list
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

def init_graph(state):
    state["time_enter_frame"] = time.time()
    state["first_shot"] = True
    state["first_hesitate"] = True
    
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
                        ("DH",u"DH_1"),
                        ("DH",u"DH_2"),
                        ("DH",u"DH_3"),
                        ("YT",u"YT_1"),
                        ("YT",u"YT_2"),
                        ("YT",u"YT_3"),
                        ("SH1",u"SH1_1"),
                        ("SH1",u"SH1_2"),
                        ("SH1",u"SH1_3"),
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
    if clip.isFinished():
        if getTimeOnFrame(state) > 1:
            if state["first_hesitate"]:
                if state["FH_state"] == 0:
                    return random.choice(getSubset(state["visited"],["FH1",]))[1]
                elif state["FH_state"] == 1:
                    if state["first_shot"]: return random.choice(getSubset(state["visited"],["FH2",]))[1]
                    else: return random.choice(getSubset(state["visited"],["FS",]))[1]
                elif state["FH_state"] == 2:
                    #alternatively, B decides to shoot self
                    return random.choice(getSubset(state["visited"],["FH3",]))[1]
                
        return "wait"
    return "-1"

def graph_waitlean(state,clip):
    if clip.isFinished():
        if getTimeOnFrame(state) > 1:
            if state["first_hesitate"]:
                return "FH4"
            else:
                #todo sec hesitate
                pass
    else: return "-1"
    
def graph_intro(state,clip):
    if clip.isFinished(): return "wait"
    else: return "-1"
    
def FH_generic(state,clip,name):
    if clip.isFinished():
        #remove the element because we've been there already
        removeElementFromSet(state["visited"],name) 
        #advance state
        state["FH_state"] += 1
        return "wait"
    else: return "-1"
def FH3_generic(state,clip,name):
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
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_fuckyou(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_BprepareshootB(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_DH_1(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_DH_2(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_DH_3(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_BshootsB(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_Bdies(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_youwin(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_YT_1(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_YT_2(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_YT_3(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_continue(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_youlose(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_SH1_1(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_SH1_2(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_SH1_3(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
def graph_SH2(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
    
    
#player functions
def graph_eyes_closing(state,clip):
    if clip.isFinished(): return "-1"
    else: return "-1"
