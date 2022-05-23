PROGRAM NIE ZADZIAŁA
NALEŻY POBRAĆ PLIKI .LAS
UMIEŚCIĆ W LINIJKACH 13, 14 FTP_script_1.py


Manualne przycinanie chmury punktów
    Etapy przetwarzania danych:
    (0) Manualne zdefiniowanie widoku poprzez obrót myszka lub:
    (0.1) Podwójne wciśnięcie klawisza X - zdefiniowanie widoku ortogonalnego względem osi X
    (0.2) Podwójne wciśnięcie klawisza Y - zdefiniowanie widoku ortogonalnego względem osi Y
    (0.3) Podwójne wciśnięcie klawisza Z - zdefiniowanie widoku ortogonalnego względem osi Z
    (1) Wciśnięcie klawisza K - zmiana na tryb rysowania
    (2.1) Wybór zaznaczenia poprzez wciśnięcie lewego przycisku myszy i 
      interaktywnego narysowania prostokąta lub
    (2.2) przytrzymanie przycisku ctrl i wybór wierzchołków poligonu lewym przyciskiem myszy
    (3) Wciśnięcie klawisza C - wybór zaznaczonego fragmentu chmury punktów i zapis do pliku
    (4) Wciśnięcie klawisza F - powrót do interaktywnego wyświetlania chmury punktów
  
Pomiar punktów na chmurze punktów
    Etapy pomiaru punktów:
    (1.1) Pomiar punktu - shift + lewy przycisk myszy
    (1.2) Cofniecie ostatniego pomiaru - shift + prawy przycisk myszy
    (2) Koniec pomiaru - wciśnięcie klawisza Q
  
Filtrowanie odchyleniem standardowym:
    (1) dla każdego punktu liczę średnią odległość do n-liczby sąsiadów
    (2) liczę średnią oraz odchylenie standardowe z wartości z poprzedniego pomiaru
    (3) ustalam parametr iloczynu odchylenia standardowego np. 1*odchylenie lub 2*odchylenie lub 0.5*odchylenie
    (4) odrzucam wszytkie punkty, które nie mieszczą się w przedziale (średnia-x*odchylenie, średnia+x*odchylenie)
  
Flitrowanie promień sfery:
    (1) dla każdego punktu wyznaczam sferę o zadanym promieniu
    (2) wyznaczam liczbę punktów, które muszą się minimalnie znaleźć w tej sferze
    (3) jeśli punkt nie ma w swojej sferze wystarczającej liczby punktów, to oznaczam go jako do odrzucenia
  
Generelizacja chmur punktów(point cloud downsampling):
    (1) voxel_down_sample(input, voxel_size) na chmurze punktów, aby otrzymać chmurę punktów z wokselami;
        woksele to pixele 3D oddalone od siebie o zadany voxel_size
    (2) uniform_down_sample usuwa co n-ty punkt(woksel?) chmury punktów
    
Podział chmur puntków na klasy metodą DBSCAN
    (1) DBSCAN (Density-Based Spatial Clustering of Application with Noise)
        to algorytm gęstościowy; zasada: dopóki liczba obiektów wokół klastra jest duża, 
        to klaster ten się powiększa
        https://en.wikipedia.org/wiki/DBSCAN
    (2) wokół punktów rysujemy okręgi o zadanym argumencie (eps) - im większe, tym łatwiej
        inne punkty się załapią jako sąsiedzi
    (3) wyznaczamy minimalną liczbę sąsiadów, żeby punkt mógł zostać uznany za corePts
    (4) jeśli punkt ma zero sąsiadów to kwalifikujemy go jako szum
    (5) jeśli punkt (0, minPts) sąsiadów, to jest zwykłym pts'm
    (6) tworzymy ciągi z corePts i pts, jeśli się łapią i nadajemy im numery
    (7) im większa liczba sąsiadów, aby punkt był corePts, tym więcej będzie klas
    
Model 3D - Ball Pivoting
    (0) punkty muszą mieć wyznaczone normalne do płaszczyzny jaką tworzą knn(k nearest neighbours), gdzie k to
        liczba naturalna (domyślnie w estimate_normals() knn=30)
    (1) kolejne punkty powierzchni leżą NA okręgu (dowolnie obróconym)
    (1.1) jeśli średnica za duża, to model nie będzie dokładny
    (1.2) jeśli średnica za mała, to model będzie dziurawy (za dokładnie będzie wszystko wyjmowane)
    
     