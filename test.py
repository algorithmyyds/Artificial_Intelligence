def uniformCostSearch(problem):
    # 作者：junruitian
    """搜索总代价最小的节点。"""
    """类似迪杰斯特拉算法。"""
    # 扩展的是路径消耗g(n)最小的节点n，用优先队列来实现，对解的路径步数不关心，只关心路径总代价。
    # 即使找到目标节点也不会结束，而是再检查新路径是不是要比老路径好，确实好，则丢弃老路径。

    start_point = problem.getStartState()  # 起始点
    queue = util.PriorityQueueWithFunction(lambda x: x[2])  # 使用优先队列按照代价排序
    queue.push((start_point, None, 0))  # 将起始点加入队列
    cost = 0  # 当前代价
    visited = []  # 记录已经访问过的节点
    path = []  # 记录路径
    parentSeq = {}  # 记录每个节点的父节点序列
    parentSeq[(start_point, None, 0)] = None  # 起始节点没有父节点
    while queue.isEmpty() == False:
        current_fullstate = queue.pop()  # 取出当前节点
        if (problem.isGoalState(current_fullstate[0])):  # 判断是否达到目标状态
            break
        else:
            current_state = current_fullstate[0]  # 当前状态
            if current_state not in visited:
                visited.append(current_state)  # 标记当前节点已访问
            else:
                continue
            successors = problem.getSuccessors(current_state)  # 获取当前节点的后继节点
            for state in successors:
                cost = current_fullstate[2] + state[2]  # 计算从起始节点到当前节点的总代价
                if state[0] not in visited:
                    queue.push((state[0], state[1], cost))  # 将后继节点加入队列
                    parentSeq[(state[0], state[1])] = current_fullstate  # 记录后继节点的父节点

    child = current_fullstate

    while (child != None):  # 从目标节点回溯到起始节点，记录路径
        path.append(child[1])  # 将当前节点加入路径
        if child[0] != start_point:
            child = parentSeq[(child[0], child[1])]  # 获取当前节点的父节点
        else:
            child = None
    path.reverse()  # 将路径反转，得到起始节点到目标节点的路径
    return path[1:]  # 返回起始节点到目标节点的路径，去掉起始节点本身
