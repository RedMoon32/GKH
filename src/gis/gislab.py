from gis.adjGraph import Graph, Vertex
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

longpoll = None
vk_session = None
vk_gis = None


def GisLab(vk, event, user, session):
    vk_gis = vk
    vk_session = session
    longpoll = VkBotLongPoll(vk_session, "183478400")
    a = adjGraphGis()
    a.GisMakeGraph(confGr)
    pfor = a.initState
    while pfor != None:
        instr = pfor[2]()
        pfor = a.GetNextFromChoice(instr)
    print("End")
    return


def gis_vk_print(ostr):
    #    print(ostr)
    vk_gis.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=mess)


def gis_vk_input(ostr):
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.obj.from_id, ' ', event.obj.text)
            if event.obj.text != '':
                if event.from_user:
                    try:
                        return event.obj.text
                    except Exception as e:
                        print(str(e))
                        continue

    # return input(ostr)
    return None


def UserEnter():
    gis_vk_print('\n - OptCostServ (OptC)')
    gis_vk_print('\n - OptTotalCost (OptT)')
    gis_vk_print('\n - Exit (X)')
    istr = gis_vk_input('\n Enter choice:')
    # return 'OptC'
    return istr


def OptCostServ():
    # cs=input('\n Введите желаемую стоимость услуги')
    gis_vk_input('\n Введите желаемую стоимость услуги=')
    return 'DownRes'


def OptTotalCost():
    # cs=input('\n Введите желаемую общую стомость')
    gis_vk_input('\n Введите желаемую общую стомость=')
    return 'DownRes'


def DownRes():
    gis_vk_print('\n Out result')
    return 'UserEnter'


def get_id_num(ent):
    return ent[0]


enter_user = {'1': ['UserEnter', UserEnter]}
opt_cost_serv = {'2': ['OptCostServ', OptCostServ]}
opt_total_cost = {'3': ['OptTotalCost', OptTotalCost]}
down_result = {'4': ['DownRes', DownRes]}

dictGR = {'1': [1, 'UserEnter', UserEnter], '2': [2, 'OptCostServ', OptCostServ],
          '3': [3, 'OptTotalCost', OptTotalCost], '4': [4, 'DownRes', DownRes]
          }

confGr = ((dictGR.get('1'), dictGR.get('2')), (dictGR.get('1'), dictGR.get('3')),
          (dictGR.get('2'), dictGR.get('4')), (dictGR.get('3'), dictGR.get('4')),
          (dictGR.get('4'), dictGR.get('1'))
          )


class adjGraphGis():
    def __init__(self):
        self.tGraph = Graph()
        self.initState = None
        self.current = self.initState

    def SetInitState(self, pin):
        self.initState = pin

    def GisMakeGraph(self, conf):
        for line in conf:
            fVertex, tVertex = line
            ifVertex = get_id_num(fVertex)
            itVertex = get_id_num(tVertex)
            self.tGraph.addEdge(ifVertex, itVertex)
        self.SetInitState(conf[0][0])
        self.currentVertices = self.tGraph.vertices[1]

    def GetNextFromChoice(self, choice_str):
        for i in self.currentVertices.adj:
            tstr = dictGR.get(str(i.id))[1]
            if (tstr.startswith(choice_str)):
                self.currentVertices = i
                return dictGR.get(str(i.id))
        return None


if __name__ == '__main__':
    class adjGraphTests():
        def __init__(self):
            self.tGraph = Graph()

        def GisMakeGraph(self, conf):
            for line in conf:
                fVertex, tVertex = line
                ifVertex = get_id_num(fVertex)
                itVertex = get_id_num(tVertex)
                self.tGraph.addEdge(ifVertex, itVertex)
            for i in self.tGraph:
                adj = i.getAdj()
                for k in adj:
                    print(dictGR.get(str(i.id)), dictGR.get(str(k.id)))


    a = adjGraphGis()
    a.GisMakeGraph(confGr)
    pfor = a.initState
    while pfor != None:
        instr = pfor[2]()
        pfor = a.GetNextFromChoice(instr)
    print("End")
