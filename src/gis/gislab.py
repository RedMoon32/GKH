from src.gis.adjGraph import Graph, Vertex
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from src.bot.vk_session import *
import sys
from src.gis.Markovec import * 

def GisLab(vk, event, user, session):
 #   vk_gis=vk
 #   vk_session=vk
 #   longpoll = VkBotLongPoll(vk_session, "183478400")
    print('GisLab starting')
    a=adjGraphGis()
    a.GisMakeGraph(confGr)
    pfor=a.initState
    while pfor != None :
        instr=pfor[2](event)
        pfor=a.GetNextFromChoice(instr)
    print("GisLab End")
    return

def gis_vk_print(ostr,event):
    vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=ostr)

def gis_vk_input(ostr,event):
    print('gis_vk_input')
    gis_vk_print(ostr,event)
    for event in longpoll.listen():
        print("longpoll")
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
    gis_vk_print("Меню ГИС",event)
    gis_vk_print("- Отопление (OptC)",event)
    gis_vk_print("- Общая стоимость услуг ЖКХ за год (OptT)",event)
    gis_vk_print('- Оптимальный портфель Марковица (MP)',event)
    gis_vk_print('- Выход (X)',event)
    istr=gis_vk_input(' Ваш выбор:',event)
    #return 'OptC'
    return istr

def printMarkovec(event):

    tstr=gis_vk_input(' Введите коэффициент допустимого риска%=',event)
    print(tstr)
    if (tstr==None): return 'DownRes'
    k_d=float(tstr)
    sol=minimize(objective,x0,method='SLSQP',\
             bounds=bnds,constraints=cons)   
    gis_vk_print("Максимум функции доходности -%s"%str(round(sol.fun,3)),event)
    gis_vk_print("ООО TKO в Тепло   - %s, доходность- %s"%(round(sol.x[0],3),round(d[0,0]*sol.x[0],3)),event)
    gis_vk_print("ООО Термо в Тепло - %s, доходность- %s"%(round(sol.x[1],3),round(d[1,0]*sol.x[1],3)),event)
    gis_vk_print("АО МонополистТепло- %s, доходность- %s"%(round(sol.x[2],3),round(d[2,0]*sol.x[2],3)),event)
    gis_vk_print("Компания 1 - %s, доходность- %s"%(round(sol.x[3],3),round(d[3,0]*sol.x[3],3)),event)
    gis_vk_print("Компания 2 - %s, доходность- %s"%(round(sol.x[4],3),round(d[4,0]*sol.x[4],3)),event)
    gis_vk_print("Компания 4 - %s, доходность- %s"%(round(sol.x[5],3),round(d[5,0]*sol.x[5],3)),event)
    return 'DownRes'

def OptCostServ(event):
    #cs=input('\n Введите желаемую стоимость услуги')
    tstr=gis_vk_input('Введите желаемую стоимость услуги=',event)
    if(tstr!=None):
        gis_vk_print('Menu ГИС->Отопление.Стоимость',event)
        gis_vk_print('1. ООО TKO в Тепло - 400 руб/ггкал',event)
        gis_vk_print('2. ООО Термо в Тепло - 600 руб/ггкал',event)
        gis_vk_print('3. АО МонополистТепло - 1759 руб/ггкал',event)
    return 'DownRes'

def OptTotalCost(event):
    #cs=input('\n Введите желаемую общую стомость')
    gis_vk_print(' Menu ГИС->Общая.Стоимость',event) 
    gis_vk_input('Введите желаемую общую стомость=',event)
    gis_vk_print(' Заглушка(Stub)',event)    
    return 'DownRes'

def DownRes(event):
    gis_vk_print(' Вывод завершен',event)
    return 'UserEnter'

def get_id_num(ent):
    return ent[0]

enter_user={'1' : ['UserEnter',UserEnter]}
opt_cost_serv={'2' : ['OptCostServ',OptCostServ]}
opt_total_cost={'3': ['OptTotalCost',OptTotalCost]}
down_result={'4' : ['DownRes',DownRes]}

dictGR={'1' : [1,'UserEnter',UserEnter],'2' : [2,'OptCostServ',OptCostServ],
        '3': [3,'OptTotalCost',OptTotalCost], '4' : [4,'Markovec',printMarkovec],'5' : [5,'DownRes',DownRes],
}

confGr=((dictGR.get('1'),dictGR.get('2')),(dictGR.get('1'),dictGR.get('3')),(dictGR.get('1'),dictGR.get('4')),
      (dictGR.get('2'),dictGR.get('5')),(dictGR.get('3'),dictGR.get('5')),(dictGR.get('4'),dictGR.get('5')),
      (dictGR.get('5'),dictGR.get('1')),
)

class adjGraphGis():
    def __init__(self):
        self.tGraph = Graph()
        self.initState=None
        self.current=self.initState
    
    def SetInitState(self,pin):
        self.initState=pin

    def GisMakeGraph(self,conf):
        for line in conf:
                fVertex, tVertex = line
                ifVertex = get_id_num(fVertex)
                itVertex = get_id_num(tVertex)
                self.tGraph.addEdge(ifVertex,itVertex)
        self.SetInitState(conf[0][0])
        self.currentVertices=self.tGraph.vertices[1]

    def GetNextFromChoice(self,choice_str):
        for i in self.currentVertices.adj:
            tstr=dictGR.get(str(i.id))[1]
            if(tstr.startswith(choice_str)):
                self.currentVertices=i
                return dictGR.get(str(i.id))
        return None

if __name__ == '__main__':
    class adjGraphTests():
        def __init__(self):
            self.tGraph = Graph()
        def GisMakeGraph(self,conf):
            for line in conf:
                fVertex, tVertex = line
                ifVertex = get_id_num(fVertex)
                itVertex = get_id_num(tVertex)
                self.tGraph.addEdge(ifVertex,itVertex)
            for i in self.tGraph:
                adj = i.getAdj()
                for k in adj:
                    print(dictGR.get(str(i.id)), dictGR.get(str(k.id)))

    a=adjGraphGis()
    a.GisMakeGraph(confGr)
    pfor=a.initState
    while pfor != None :
        instr=pfor[2]()
        pfor=a.GetNextFromChoice(instr)
    print("End")