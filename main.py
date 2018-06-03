#coding=utf-8

from camspy import netSurveillance

def scan(subnet2):
    for subnet3 in range(67,256,1):
        netSurveillance.subnetScan(subnet2,subnet3)
        
if __name__ == '__main__':
    scan(32)
