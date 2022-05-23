import open3d as o3d

#Filtracja chmur punktów metodą StatisticalOutlierRemoval
def wyznaczanie_obserwacji_odstajacych(chmura_punktow, liczba_sasiadow, std_ratio):
    chmura_punktow_odfiltrowana, ind = chmura_punktow.\
        remove_statistical_outlier(liczba_sasiadow, std_ratio)
    #ponizej zamiast select_down_sample jest select_by_index - nowsza wersja o3d
    punkty_odstajace = chmura_punktow.select_by_index(ind, invert = True)
    punkty_odstajace.paint_uniform_color([1,0,0])
    # o3d.visualization.draw_geometries([chmura_punktow_odfiltrowana, punkty_odstajace], left=5, top=30)
    return chmura_punktow_odfiltrowana, punkty_odstajace

#Filtracja chmur punktów metodą radius_outlier_removal
def wyznaczanie_obserwacji_odstajacych_radius(chmura_punktow, min_liczba_punktow, promien_sfery):
    chmura_punktow_odfiltrowana, ind = chmura_punktow.remove_radius_outlier(min_liczba_punktow, promien_sfery)
    punkty_odstajace = chmura_punktow.select_by_index(ind, invert = True)
    punkty_odstajace.paint_uniform_color([1,0,0])
    o3d.visualization.draw_geometries([chmura_punktow_odfiltrowana, punkty_odstajace], left=5, top=30)
    return chmura_punktow_odfiltrowana, punkty_odstajace