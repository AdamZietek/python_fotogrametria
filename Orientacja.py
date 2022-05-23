from cmath import atan
from math import atan2
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import copy
from Interakcja import *

#Orientacja metodą Target-based
def wyswietlanie_par_chmur_punktow(chmura_referencyjna,chmura_orientowana,transformacja):
    ori_temp = copy.deepcopy(chmura_orientowana)
    ref_temp = copy.deepcopy(chmura_referencyjna)
    ori_temp.paint_uniform_color([1, 0, 0])
    ref_temp.paint_uniform_color([0, 1, 0])
    ori_temp.transform(transformacja)
    o3d.visualization.draw_geometries([ori_temp, ref_temp])

def orientacja_target_based(chmura_referencyjna, chmura_orientowana, typ = 'Pomiar', Debug = 'True'):
    print('Orientacja chmur punktów metoda Target based')
    wyswietlanie_par_chmur_punktow(chmura_referencyjna, chmura_orientowana, np.identity(4))
    if typ != 'File':
        print('Pomierz min. 3 punkty na chmurze referencyjnej: ')
        pkt_ref = pomiar_punktow_na_chmurze(chmura_referencyjna)
        print('Pomierz min. 3 punkty orientowanej ')
        pkt_ori = pomiar_punktow_na_chmurze(chmura_orientowana)
    elif typ == 'Plik':
        print('Wyznaczenia parametrów transformacji na podstawie punktów pozyskanych z plików tekstowych')
    #Wczytanie chmur punktów w postaci plików tekstowych
    #Przygotowanie plików ref i ori
    else: #Inna metoda
        print('Wyznaczenie parametrów na podstawie analizy deskryptorów')
        #Analiza deskryptorów
    assert (len(pkt_ref) >= 3 and len(pkt_ori) >= 3)
    assert (len(pkt_ref) == len(pkt_ori))
    corr = np.zeros((len(pkt_ori), 2))
    corr[:, 0] = pkt_ori
    corr[:, 1] = pkt_ref
    print(f'corr = {corr}')
    p2p = o3d.pipelines.registration.TransformationEstimationPointToPoint()
    trans = p2p.compute_transformation(chmura_orientowana, chmura_referencyjna, o3d.utility.Vector2iVector(corr))
    if Debug == 'True':
        print(trans)
        wyswietlanie_par_chmur_punktow(chmura_referencyjna, chmura_orientowana, trans)
    return(trans)