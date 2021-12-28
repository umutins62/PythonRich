# -*- coding: utf-8 -*-

import math

from rich.console import Group
from rich.panel import Panel
from datetime import datetime
from rich.prompt import Prompt

from rich.markdown import Markdown
from rich import print
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
import sys

console = Console()
hp = 0.00



while True:
    panel_group = Group(
        Panel(
            "Hidrolik Hesap                                                                       " + str(
                datetime.now().date()), style="on blue"),
    )
    print(panel_group)



    dere_adi = Prompt.ask("Dere Adı")
    n = float(Prompt.ask("Pürüzlülük (n)").replace(",", "."))
    Q100 = float(Prompt.ask("Q100 Debisi").replace(",", "."))
    Q500 = float(Prompt.ask("Q500 Debisi").replace(",", "."))

    memba = float(Prompt.ask("Memba Kotu").replace(",", "."))
    mansap = float(Prompt.ask("Mansap Kotu").replace(",", "."))
    Ldere = float(Prompt.ask("Dere Uzunluğu").replace(",", "."))

    j = round((memba-mansap)/Ldere,4)
    m = float(Prompt.ask("Şev Eğimi(1/m)").replace(",", "."))
    b = float(Prompt.ask("Dere Genişliği(b)").replace(",", "."))

    QH = 0.00
    H = 0.00
    d = 0.0001
    while QH <= Q100:
        ze = d
        H = H + ze
        F = (m * H + b) * H
        P = math.sqrt(pow(m * H, 2) + pow(H, 2)) * 2 + b
        R = F / P
        T = 1000 * R * j
        V = pow(R, (2 / 3)) * pow(j, (1 / 2)) / n
        HV = pow(V, 2) / (2 * 9.81)
        QH = V * F

    # console.print("H100: "+str(round(HV,2))+" m",style="Green")

    QH1 = 0.00
    H1 = 0.00
    d1 = 0.0001
    while QH1 <= Q500:
        ze1 = d1
        H1 = H1 + ze1
        F1 = (m * H1 + b) * H1
        P1 = math.sqrt(pow(m * H1, 2) + pow(H1, 2)) * 2 + b
        R1 = F1 / P1
        T1 = 1000 * R1 * j
        V1 = pow(R1, (2 / 3)) * pow(j, (1 / 2)) / n
        HV1 = pow(V1, 2) / (2 * 9.81)
        QH1 = V1 * F1


    # console.print("H500: "+str(round(HV1,2))+" m",style="Green")

    # user_renderables = [Panel("H100:"+str(round(HV,2))+" m")]
    # print(Columns(user_renderables))
    #
    # user_renderables1 = [Panel("H500:"+str(round(HV1,2))+" m")]
    # print(Columns(user_renderables1))

    def havapayihesabi(V, h):
        global hp
        hp = round(0.60 + (0.03731 * V * pow(h, (1 / 3))), 3)
        return hp


    hp1 = havapayihesabi(V, H)
    hp2 = havapayihesabi(V1, H1)
    # print(str(hp))

    table = Table(title=dere_adi + " Deresi Hidrolik Hesap Tablosu")

    # Veriler
    table.add_column("Q\nYıl", justify="center", style="Green")
    table.add_column("Q\nGelen", justify="center", style="Green")
    table.add_column("J\n(Eğim)", justify="center", style="Green")
    table.add_column("1/m", justify="center", style="Green")
    table.add_column("n\n(Pürüzlülük)", justify="center", style="Green")
    table.add_column("b\n(Dere Açıklığı)", justify="center", style="Green")
    # Hesap Edilenler
    table.add_column("h", justify="center", style="#FF7A33")
    table.add_column("F", justify="center", style="#FF7A33")
    table.add_column("P", justify="center", style="#FF7A33")
    table.add_column("R", justify="center", style="#FF7A33")
    table.add_column("V", justify="center", style="#FF7A33")
    table.add_column("Q\nHesap", justify="center", style="#FF7A33")
    table.add_column("T\n(Sürüntü Miktarı)", justify="center", style="#FF7A33")
    table.add_column("V2/2g", justify="center", style="#FF7A33")
    table.add_column("Hava\nPayı", justify="center", style="#FF7A33")
    table.add_column("Seçilen\nYükseklik", justify="center", style="Green")

    secilen100 = 0.00
    secilen500 = 0.00
    if H + hp >= H1:
        secilen100 = round(H + hp, 2)
    else:
        secilen100 = round(H1, 2)

    table.add_row("100", str(Q100), str(j), str(m), str(n), str(b), str(round(H, 2)), str(round(F, 2)),
                  str(round(P, 2)), str(round(R, 2)), str(round(H, 2)), str(round(QH, 2)), str(round(T, 2)),
                  str(HV), str(hp1), str(secilen100))
    table.add_row("500", str(Q500), str(j), str(m), str(n), str(b), str(round(H1, 2)), str(round(F1, 2)),
                  str(round(P1, 2)), str(round(R1, 2)), str(round(H1, 2)), str(round(QH1, 2)), str(round(T1, 2)),
                  str(HV1), str(hp2), str(secilen100))


    console = Console()
    console.print(table)

    r=40.0
    h4 =float(H)
    ysaliyman=round(0.3*h4,2)
    yskurp1=round(h4*(1.8-0.0051*(r/b)+(0.0084*(b/h4)))-h4,2)
    yskurp2=round(h4*(2.15*0.27*math.log((r/b)-2))-h4,2)

    listeys=[]
    listeys.append(ysaliyman)
    listeys.append(yskurp1)
    listeys.append(yskurp2)
    enbuyuk=max(listeys)



    table1 = Table(title=dere_adi + " Deresi Oyulma Derinliği Hesabı")

    table1.add_column("R", justify="center", style="Green")
    table1.add_column("W", justify="center", style="Green")
    table1.add_column("Aliyman", justify="center", style="Green")
    table1.add_column("KURB(MAYNORD)", justify="center", style="Green")
    table1.add_column("KURB(THORNE)", justify="center", style="Green")

    table1.add_row(str(r), str(b), str(ysaliyman), str(yskurp1), str(yskurp2))
    console.print(table1)

    console.print("Temel Yüksekliği Maksimum Oyulma Derinliği :"+str(enbuyuk)+" m den yüksek olmalıdır.",style="Green")

    if V>5 :
        console.print("V(Hız): "+str(round(V,2))+" > 5 olduğundan önlem alınmalıdır(Dere içerisinde brit veya şut yapılmalıdır).",style="Red")

    else:
        console.print("V(Hız): "+str(round(V,2))+" < 5 olduğundan önlem alınmasına gerek yoktur.",style="Green")


    if T>12 :
        console.print("T(sürüntü): "+str(round(T,2))+" > 12 olduğundan önlem alınmalıdır(Dere içerisinde brit veya şut yapılmalıdır).",style="Red")

    else:
        console.print("T(sürüntü): "+str(round(T,2))+" < 12 olduğundan önlem alınmasına gerek yoktur.",style="Green")




    onay = Prompt.ask("Başa dönmek istiyormusunuz E/H ")
    if onay == "E" or onay == "e":
        break

    elif onay == "H" or onay == "h":
        continue
    else:
        console.print("Lütfen bir seçim yapınız", style="#FF7A33")





