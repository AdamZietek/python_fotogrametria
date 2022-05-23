# Import potrzebnych plikow
from Wstep import *
from Interakcja import *
from Filtracja import *
from Generalizacja import *
from Klasteryzacja import *
from Modelowanie import *
from Orientacja import *

def main():
    
    # 1_WSTEP
    chmura_dj = r"chmura_dj.las"
    chmura_zdjecia_naziemne = r"chmura_zdjecia_naziemne.las"
    chmura_punktow_dj = wczytanie_chmury_punktow_las_konwersja_do_o3d(chmura_dj)
    chmura_punktow_naziemne = wczytanie_chmury_punktow_las_konwersja_do_o3d(chmura_zdjecia_naziemne)
    
    # 2_INTERAKCJA
    # manualne_przycinanie_chmury_punktow(chmura_punktow_dj)
    # obliczanie_obszaru_opracowania(chmura_punktow_dj, typ = 'AxisAlignedBoundingBox')
    # pomiar_punktow_na_chmurze(chmura_punktow_dj)

    # 3_FILTRACJA
    # pkt_odfiltrowane_dj, pkt_odstajace_dj = wyznaczanie_obserwacji_odstajacych_radius(chmura_punktow_dj, min_liczba_punktow = 30, promien_sfery = 2.0)
    # chmura_punktow_dj, pkt_odstajace_dj = wyznaczanie_obserwacji_odstajacych(chmura_punktow_dj, liczba_sasiadow = 20, std_ratio = 0.5)
    # chmura_punktow_naziemne, pkt_odstajace_naziemne = wyznaczanie_obserwacji_odstajacych(chmura_punktow_naziemne, liczba_sasiadow = 20, std_ratio = 0.5)

    # 4_GENERALIZACJA
    # regularyzacja_chmur_punktow(chmura_punktow_dj, 0.1)
    # usuwanie_co_n_tego_punktu_z_chmury_punktow(chmura_punktow_dj, 10)

    # 5_KLASTERYZACJA
    # klasteryzacja_DBSCAN(chmura_punktow_dj, 0.5, 10)
    
    # 6_MODELOWANIE
    promienie_kul = [0.2, 0.5, 1]
    ball_pivoting(chmura_punktow_dj, promienie_kul)
    
    # 8_ORIENTACJA
    # orientacja_target_based(chmura_punktow_dj, chmura_punktow_naziemne)
    
if __name__ == "__main__":
    main()
    