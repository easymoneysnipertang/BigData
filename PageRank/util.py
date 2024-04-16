import networkx as nx


def read_data(path):
    # 读取数据，返回图的边集，点的个数，点集
    file = open(path, 'r')
    graph=[] 
    node_set=set()
    for line in file:
        data=line.split()
        edge=(int(data[0]),int(data[1]))  # 以tuple存储两个点/边
        node_set.add(edge[0])
        node_set.add(edge[1])
        graph.append(edge)

    node_num=len(node_set) # 点的个数
    return graph, node_num, node_set


def check_continuous(node_set, node_num):
    # 验证点的序号是否为 1-node_num
    for i in range(1,node_num+1):
        if i not in node_set:
            print('点的序号不连续')
            return False
    print('点的序号连续')
    return True


def standard_answer(G,alpha=0.85,tol=1e-6):
    # 使用networkx得到的标准答案
    testG = nx.DiGraph()
    for edge in G:
        testG.add_edge(edge[0], edge[1])
    print(f"节点数: {len(testG.nodes)}")

    pr = nx.pagerank(testG, alpha=alpha, tol=tol/len(testG))
    # 对 pagerank 值进行排序
    sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)
    # 计算所有节点pagerank值之和
    pr_sum = sum(pr.values())
    print(f"所有节点pagerank值之和: {pr_sum}")

    # 保存前100个节点的pagerank值
    standard_result = {}
    for i in range(100):
        standard_result[sorted_pr[i][0]] = sorted_pr[i][1]
    return standard_result


def write_result(sorted_indices, sorted_scores, filename):
    # 将结果写入文件
    path = 'results/' + filename
    with open(path, 'w') as file:
        for i in range(len(sorted_indices)):
            file.write(str(sorted_indices[i]+1) + ' ' + str(sorted_scores[i]) + '\n')