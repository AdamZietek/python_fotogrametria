import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

#Klasteryzacja punktów algorytmem DBSCAN
def klasteryzacja_DBSCAN(chmura_punktow, odleglosc_miedzy_punktami, min_punktow, progress = True):
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        klasy = np.array(chmura_punktow.cluster_dbscan(odleglosc_miedzy_punktami,\
                         min_punktow, progress))    
    liczba_klas = klasy.max()+1
    print("Algorytm DBSCAN wykrył %i klas" % liczba_klas)
    print("Rozmiar tablicy to %i punktów" % klasy.size) 
    paleta_barwna_kolorow = plt.get_cmap("tab20")(klasy/(klasy.max() if klasy.max() > 0 else 1))
    
    paleta_barwna_kolorow[klasy < 0] = 0
    chmura_punktow.colors = o3d.utility.Vector3dVector(paleta_barwna_kolorow[:, :3])
    o3d.visualization.draw_geometries([chmura_punktow], left=5, top=30)
