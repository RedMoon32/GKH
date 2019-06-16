from gis.adjGraph import Graph, Vertex
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from src.secrets import token

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "183478400")


def GisLab(vk, event, user, session):
    #   vk_gis=vk
    #   vk_session=vk
    #   longpoll = VkBotLongPoll(vk_session, "183478400")

    a = adjGraphGis()
    a.GisMakeGraph(confGr)
    pfor = a.initState
    while pfor != None:
        instr = pfor[2](event)
        pfor = a.GetNextFromChoice(instr)
    print("End")
    return


def gis_vk_print(ostr, event):
    #    print(ostr)
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=ostr)

>> >> >> > 0
84
c99046c76ac167f7a734ac663ef4a1e3ce3b6


def gis_vk_input(ostr, event):
    print('gis_vk_input')
    gis_vk_print(ostr, event)
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


def UserEnter(event):
    gis_vk_print('\n Меню ГИС', event)
    gis_vk_print('\n - Отопление (OptC)', event)
    gis_vk_print('\n - Общая стоимость услуг ЖКХ за год (OptT)', event)
    gis_vk_print('\n - Выход (X)', event)
    istr = gis_vk_input('\n Ваш выбор:', event)
    # return 'OptC'
    return istr


def OptCostServ(event):
    # cs=input('\n Введите желаемую стоимость услуги')
    tstr = gis_vk_input('\n Введите желаемую стоимость услуги=', event)
    if (tstr != None):
        gis_vk_print('\n Menu ГИС->Отопление.Стоимость', event)
        gis_vk_print('\n 1. ООО TKO в Тепло - 400 руб/ггкал', event)
        gis_vk_print('\n 2. ООО Термо в Тепло - 600 руб/ггкал', event)
        gis_vk_print('\n 3. АО МонополистТепло - 1759 руб/ггкал', event)
    return 'DownRes'


def OptTotalCost(event):
    # cs=input('\n Введите желаемую общую стомость')
    gis_vk_input('\n Введите желаемую общую стомость=', event)
    return 'DownRes'


def DownRes(event):
    gis_vk_print('\n Вывод завершен', event)
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
