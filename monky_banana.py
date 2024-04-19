# -*- coding: utf-8 -*-

# State类，记录当前状态
class State:
    def __init__(self, monkey=-1, box=0,banana=1, monbox=-1,holds=-1,hang_banana=1):
        self.monkey = monkey  # -1:Monkey at A  0: Monkey at B  1:Monkey at C
        self.box = box      # -1:box at A  0:box at B  1:box at C
        self.banana = banana   # Banana at C,Banana=1
        self.monbox = monbox  # -1: monkey not on the box  1: monkey on the box
        self.holds=holds
        self.hang_banana=hang_banana
# 复制前一个状态情况给当前状态，注意不是将对象直接复制，而是创建新的对象复制原状态的数据
def copyState(source):
    state = State()
    state.monkey = source.monkey
    state.box = source.box
    state.banana = source.banana
    state.monbox = source.monbox
    return state

# function monkeygoto,it makes the monkey goto the other place
def monkeygoto(b,i):
    if States[i].monbox==-1 and States[i].monkey!=b:
        a=b
        if (a==-1):
            routesave.append("Monkey go to A")
        elif a==0:
            routesave.append("Monkey go to B")
        else:
            routesave.append('"Monkey go to C"')
        States[i].monkey=b
    else:
        return




# function movebox,the monkey move the box to the other place
def movebox(a,i):
    b = a
    if(States[i].monkey==States[i].box and States[i].monbox==-1 and States[i].box!=a):
        if b==-1:
            routesave.append("Monkey move box to A")
        elif b==0:
            routesave.append("Monkey move box to B")
        else:
            routesave.append("Monkey move box to C")
        States[i].box = a
        States[i].monkey=a
    else:
        return




# function climbonto,the monkey climb onto the box
def climbonto(i):
    if States[i].monbox == -1 and States[i].monkey == States[0].banana and States[i].box==States[0].banana:
        routesave.append( "Monkey climb onto the box")
        States[i].monbox=1
    else:
        return

# function climbdown,monkey climb down from the box
def climbdown(i):
    if States[i].monbox==1 and States[i].monkey!=States[0].banana:
        routesave.append("Monkey climb down from the box")
        States[i].monbox=-1


# function reach,if the monkey,box,and banana are at the same place,the monkey reach banana
def reach(i):
    if States[i].monbox==1 and States[i].box==States[0].banana and States[i].hang_banana==1 and States[i].holds==-1:
        routesave.append("Monkey reach the banana")
        States[i].holds=1
        States[i].hang_banana=-1
    else:
        return
# output the solution to the problem
def showSolution(i):
    print ("Result to problem:")
    for c in range(len(routesave)):
        print("Step %d : %s \n"%(c+1,routesave[c]))
# perform next step
def nextStep(i):
    #print States[i].box
    if(i>=150):
        showSolution(i)
        print("%s  \n", "steplength reached 150,have problem ")
        exit(0)

    # 如果满足条件，就输出结果
    if(States[i].holds ==1):
        showSolution(i)
        exit(0)
    else:
        States[i+1]=copyState(States[i])
        climbdown(i+1)
        monkeygoto(States[i].box,i+1)
        movebox(States[0].banana,i+1)
        climbonto(i+1)
        reach(i + 1)





if __name__ == "__main__":
    s = input("please input state: monkey, box, banana, ifMonkeyIsOnBox: \n")
    '''
           下面利用States列表存储每一步的states的状态，即每一步各个实体的位置
           routesave列表存储每一步进行的操作描述，如：Monkey go to A
    '''
    states = s.split(" ")
    state = State(int(states[0]), int(states[1]), int(states[2]), int(states[3]))
    States = [None]*150
    routesave = []
    States.insert(0,state)
    i=0
    while(True):
        nextStep(i)
        i=i+1