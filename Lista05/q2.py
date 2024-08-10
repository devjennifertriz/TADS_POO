from datetime import datetime
import enum

class Boleto:
    def __init__(self, codBarras, dataEmiss, dataVencimento, dataPagto, valorBoleto):
        self.__codBarras = codBarras
        self.__dataEmiss = dataEmiss
        self.__dataVencimento = dataVencimento
        self.__dataPagto = dataPagto
        self.__valorBoleto = valorBoleto

    ## SETS & GETS
    def setCodBarras(self, codBarras):
        self.__codBarras = codBarras

    def setDataEmiss(self, dataEmiss):   
        self.__dataEmiss = dataEmiss

    def setDataVencimento(self, dataVencimento):
        self.__dataVencimento = dataVencimento

    def setDataPagto(self, dataPagto):
        self.__dataPagto = dataPagto

    def setValorBoleto(self, valorBoleto):
        self.__valorBoleto = valorBoleto

    def setValorPago(self, valorPago):
        self.__valorPago = valorPago

    def getCodBarras(self):
        return self.__codBarras
    
    def getDataEmisss(self):
        return self.__dataEmiss
    
    def getDataVencimento(self):
        return self.__dataVencimento
    
    def getDataPagto(self):
        return self.__dataPagto
    
    def getValorBoleto(self):
        return self.__valorBoleto
    
    def getValorPago(self):
        return self.__valorPago
    
    ##MÉTODOS
    
    def setSituacaoPagamento(self):
        self.__situacaoPagamento = Pagamento()
    
    def getSituacaoPagamento(self):
        return self.__situacaoPagamento

    def Pagar(self, valorPago):
        if self.__valorPago > 0: self.__valorPago = valorPago
        return self.__valorBoleto - valorPago

    def Situacao(self):
        Pagamento()

    def __str__(self):
        return f'Boleto [{self.__codBarras}] == Emissão: {self.__dataEmiss} == Vencimento: {self.__dataVencimento} == Data de Pagamento: {self.__dataPagto}'
    
class Pagamento(enum.Enum):
    EmAbert = 1
    PagoParcial = 2
    Pago = 3