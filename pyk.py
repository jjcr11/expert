from pyknow import *

class Sospecha(Fact):
    """ Ask about suspicions """


class Sintomas1(Fact):
    """Ask about minor symptoms"""


class Sintomas2(Fact):
    """Ask about medium symptoms"""


class Sintomas3(Fact):
    """Ask about so f*cking severe symptoms"""


class UltimosDias(Fact):
    """Ask about symptoms in last seven days"""


class Solution(KnowledgeEngine):
    @Rule(Sospecha(sospecha='no'))
    def notSuspicions(self):
        print(
            "----------------------------------------------------------------------------------------------------------")
        print(
            "Limita tu exposición a sitios concurridos, Mantén una Sana Distancia." + '\n' + "Te invitamos a mantenerte informada(o) de las medidas de prevención comunicadas por la Secretaría de Salud Federal en www.gob.mx/coronavirus")

    @Rule(Sospecha(sospecha='si'))
    def yesSuspicions(self):
        self.declare(Sintomas1(ask_symptoms1=input(
            "¿Tú o esta persona tienen al menos dos de los siguientes síntomas? Tos, fiebre o dolor de cabeza. (sí / no): ")))
        print()

    @Rule(Sintomas1(ask_symptoms1='si'))
    def yesSymptoms1(self):
        self.declare(Sintomas2(ask_symptoms2=input(
            "¿Además se acompaña de al menos uno de los siguientes? Dolor o ardor de garganta, escurrimiento nasal, ojos rojos o dolor de músculos o articulaciones. (sí / no): ")))
        print()

    @Rule(Sintomas1(ask_symptoms1='no'))
    def notSymptoms1(self):
        self.declare(UltimosDias(ask_lastDays=input(
            "¿En los últimos 7 días la persona ha presentado tos, dolor de garganta, dolor de cabeza y/o fiebre igual o mayor a 38°C? (sí / no): ")))
        print()

    @Rule(Sintomas2(ask_symptoms2='si'))
    def yesSymptoms2(self):
        self.declare(Sintomas3(ask_symptoms3=input(
            "Tienes los síntomas del COVID-19 ¿Además presentas dificultad para respirar o dolor en el pecho? (sí / no): ")))
        print()

    @Rule(Sintomas2(ask_symptoms2='no'))
    def notSymptoms2(self):
        print(
            "----------------------------------------------------------------------------------------------------------")
        print(
            "Se trata de un cuadro leve, quédate en casa y aíslate en lo posible de tu familia para no contagiarlos. No olvides que si empiezas a tener dificultad para respirar, dolor en el pecho o la fiebre no se baja en varios días, necesitas recibir atención médica inmediata." + '\n' + "Si eres una persona adulta mayor o vives con diabetes, hipertensión, obesidad, cáncer, VIH o alguna deficiencia de tu sistema inmunológico (trasplante de órganos), o si eres una persona embarazada, perteneces a  los grupos de riesgo y también debes ser revisado por personal de salud.")

    @Rule(Sintomas3(ask_symptoms3='si'))
    def yesSymptoms3(self):
        print(
            "----------------------------------------------------------------------------------------------------------")
        print("Se trata de un cuadro que puede ser grave, llama al 911.")

    @Rule(Sintomas3(ask_symptoms3='no'))
    def notSymptoms3(self):
        print(
            "----------------------------------------------------------------------------------------------------------")
        print(
            "Se trata de un cuadro leve, quédate en casa y aíslate en lo posible de tu familia para no contagiarlos. No olvides que si empiezas a tener dificultad para respirar, dolor en el pecho o la fiebre no se baja en varios días, necesitas recibir atención médica inmediata." + '\n' + "Si eres una persona adulta mayor o vives con diabetes, hipertensión, obesidad, cáncer, VIH o alguna deficiencia de tu sistema inmunológico (trasplante de órganos), o si eres una persona embarazada, perteneces a  los grupos de riesgo y también debes ser revisado por personal de salud.")

    @Rule(UltimosDias(ask_lastDays='si'))
    def yesLastDays(self):
        print(
            "----------------------------------------------------------------------------------------------------------")
        print(
            "Quédate en casa hasta cumplir 14 días después de iniciados los síntomas. Después de este periodo, evita sitios concurridos y mantén una Sana Distancia." + '\n' + "Te invitamos a mantenerte informada(o) de las medidas de prevención comunicadas por la Secretaría de Salud Federal en www.gob.mx/coronavirus")

    @Rule(UltimosDias(ask_lastDays='no'))
    def notLastDays(self):
        print(
            "----------------------------------------------------------------------------------------------------------")
        print(
            "Limita tu exposición a sitios concurridos, Mantén una Sana Distancia." + '\n' + "Te invitamos a mantenerte informada(o) de las medidas de prevención comunicadas por la Secretaría de Salud Federal en www.gob.mx/coronavirus")


engine = Solution()
engine.reset()

ask_sospecha = input(
    "Hola! Soy Susiano Distancia, ya sabrás quien es mi novia. Vengo a ayudarte a diagnosticar si tienes coronavirus a través de tus síntomas. Empecemos!" + '\n' + "¿Sospechas que tienes coronavirus o alguien cercano a ti puede tenerlo? (sí / no): ")
print()

engine.declare((Sospecha(sospecha=ask_sospecha)))

engine.run()