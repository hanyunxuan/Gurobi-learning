if __name__ == '__main__':
    from gurobipy import *

    m = Model()
    # 建立3*4维度的01变量
    x = m.addVars(3, 4, vtype=GRB.BINARY, name="x")
    # 建立i维度所有的求和小于1
    m.addConstrs((x.sum(i, '*') <= 1 for i in range(3)), name="con")
    m.update()
    m.write("test.lp")
    print(1)
