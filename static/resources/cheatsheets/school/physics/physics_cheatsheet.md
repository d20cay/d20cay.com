# Physik Cheatsheet

[TOC]

## Hydrostatik

Druck ist keine gerichtete Grösse!

$p$: Druck [$\frac{N}{m^2}$]
$\rho$: Dichte [$\frac{kg}{m^3}$]

$p_0$: Luftdruck [$\frac{N}{m^2}$]
$\Delta p$: Hydrostatischer Druck/Überdruck [$\frac{N}{m^2}$]
$$
\Delta p = \rho _{Fl} \cdot g \cdot h \\
p(h) = p_0 + \Delta p = p_0 + \rho _{Fl} \cdot g \cdot h \\
$$

### Auftriebskraft

$F_A$: Auftriebskraft [$N$]
$V$: *eingetauchtes* Volumen des Körpers [$m^3$]
$\rho _K$: *mittlere* Dichte eines Körpers [$\frac{kg}{m^3}$]
$$
F_A = \rho _{Fl} \cdot V \cdot g
$$
Schwimmen:
$$
\rho _K < \rho _{Fl} \\
F_A = F_G
$$
Schweben:
$$
\rho _K = \rho _{Fl} \\
F_A = F_G
$$
Sinken:
$$
\rho _K > \rho _{Fl} \\
F_A < F_G
$$

## Wärme

$Q$: Wärmeenergie [$J$]
$$
\Delta Q = m c \cdot \Delta T  \\
0 K = -273.15 ^\circ C
$$

### Wärmekapazität

$c$: spez. Wärmekapazität [$\frac{J}{kg \cdot K}$]
$$
C = m_1 \cdot c_1 + m_2 \cdot c_2 + ... \\
\Delta Q = m \cdot c \cdot \Delta T \\
\Delta Q = C \cdot \Delta T \\~\\

\Delta Q_{zu} = \Delta Q_{ab} \\
m_1 \cdot c_1 \cdot (T_1 - T_M) = m_2 \cdot c_2 \cdot (T_2 - T_M)
$$

$\Delta Q_f$: Schmelzwärme [$J$]
$\Delta Q_v$: Verdampfungswärme [$J$]
$L_f$: Schmelzwärme [$\frac{J}{kg}$]
$L_v$: Verdampfungswärme [$\frac{J}{kg}$]

<img style="width: 40%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\phase_transitions.png">
$$
\Delta Q_f = m \cdot L_f \\
\Delta Q_v = m \cdot L_v
$$

### Längenausdehnung

$\alpha$: Längenausdehnungskoeffizient [$\frac{1}{K}$]
$$
\Delta l = l_0 \cdot \alpha \cdot \Delta T \\
l = l_0 \cdot (1 + \alpha \cdot \Delta T) \\~\\
\Delta V = V_0 \cdot \gamma \cdot \Delta T \\
V = V_0 \cdot (1 + \alpha \cdot \Delta T)
$$

### Gasgesetze

Solange $T$ *konstant*:
$$
p_1 \cdot V_1 = p_2 \cdot V_2 \\
p_3 \cdot V_3 = p_1 \cdot V_1 + p_2 \cdot V_2
$$
Solange $p$ konstant:
$$
\frac{V_1}{T_1} = \frac{V_2}{T_2}
$$
Allgemein:

$R_S$: spezifische Gaskonstante [$\frac{J}{kg \cdot K}$]
$R$: allg. Gaskonstante = $8.314 \frac{J}{kg \cdot K}$
$n$: Stoffmenge [$mol$]
$$
\frac{p_1 \cdot V_1}{T_1} = \frac{p_2 \cdot V_2}{T_2} \\
\frac{p \cdot V}{T} = m \cdot R_S \\
\frac{p \cdot V}{T} = n \cdot R
$$

### Wärme aus Reibung

$$
F_R \cdot s = m c \cdot \Delta T
$$

## Mechanik

### Kräfte

Einheit: [N]<br>Formelzeichen: F
$$
F = m * g
$$

#### Kräftegleichgewicht

$$
\vec{F}_{res} = \vec{F_1} + \vec{F_2} + \vec{F_3} = 0
$$

### Drehmoment

Einheit: [Nm]<br>Formelzeichen: M

$M_r$ = Drehmoment nach rechts

$M_l$ = Drehmoment nach links
$$
\begin{align*}
M_r &= M_l \\
M_r &= F_1*l_1 + F_2*l_2 \cdots\\
M_l &= F_3*l_3 + F_4*l_4 \cdots
\end{align*}
$$

### Reibung

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\friction.png">

$F_R$: (maximal mögliche) Reibungskraft [N]

$F_N$: Normalkraft [N] (Reaktionskraft)

$μ$: Reibungskoeffizient

Solange keine Kraft auf den Körper drückt, gilt $F_N = F_G$
$$
\mu = \frac{F_R}{F}\\
F_R = \mu \cdot F_N
$$

#### Abhang & Reibung

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\inclined_friction.png">

$F_H$: Hangabtriebskraft [N]

$F_{G⊥}$: Kraft senkrecht zur Ablage [N]
$$
\begin{align*}
F_H &= F_G \cdot \sin(\alpha) \\
F_N &= F_{G⊥} = F_G \cdot \cos(\alpha) \\
F_R &= μ \cdot F_N \\
F_R &= μ \cdot F_G \cdot \cos(\alpha)
\end{align*}
$$

Wenn $F_h = F_R$ gilt, gilt auch
$$
FG \cdot \sin(\alpha) = \mu \cdot F_G \cdot \cos(\alpha) \\
\sin(\alpha) = \mu \cdot \cos(\alpha) \\
\mu = \frac{\sin(\alpha)}{\cos(\alpha)} \\
\mu = \tan(\alpha) \\
$$


## Geschwindigkeit

$a$: Beschleunigung [$\frac{m}{s^2}$]

$v$: Geschwindigkeit [$\frac{m}{s}$]

$t$: Zeit [$s$]

$s$: Strecke [m]

**Mit Anfangsgeschwindigkeit**

$v_0$: Anfangsgeschwindigkeit [$\frac{m}{s}$]
$$
v = \sqrt{v_0^2 + 2 a s}\\
v(t) = a t + v_0
$$
**Ohne Anfangsgeschwindigkeit**
$$
v = a t\\
v = \sqrt{2 a s}\\
v = \sqrt{v_0^2 + 2 a s}\\
v = a t
$$

### Beschleunigung

$$
a = \frac{\Delta v}{\Delta t}
$$

### Strecke

$$
s = v \cdot t \\
s = \frac{1}{2} a t^2\\
s(t)= s_0 + v_0 \cdot t + \frac{1}{2} a t^2
$$

### Zeit

$$
t = \frac{s}{v} \\
t = \frac{s}{\overline{v}} = \frac{2s}{v1+v2}
$$

### 2. Newtonsches Axiom

$$
F_{Res}  = ma
$$



## Arbeit

$W$: Arbeit/Energie [$Nm$/$J$/$Ws$]

Arbeit = Kraft (in Wegrichtung) * Strecke
$$
W = F \cdot s
$$

### Leistung

$P$: Leistung [$W$]

Leistung = Kraft (in Wegrichtung) * Geschwindigkeit (* Reibungskoeffizient) pro Zeit
$$
P = \frac{\Delta E}{t} \\
P = F \cdot v \\
P = F \cdot v \cdot \mu
$$


### Wirkungsgrad

Der Wirkungsgrad stellt die Übersetzung von aufgewandter Energie zu gebrauchter Energie dar. Er ist ein Mass der Effizienz.
$$
\eta = \frac{E_{Nutzen}}{E_{Aufwand}}
$$

### Hubarbeit/Potentielle Energie

$$
W_H = F \cdot s = m \cdot g \cdot s = E_{pot}
$$

### Spannarbeit/Federenergie

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\federenergie.png">

$D$: Federkonstante [$\frac{N}{m}$]
$$
F_F = D \cdot \Delta x \\
W_S = \frac{1}{2}D \cdot {\Delta x}^2 = E_F
$$

### Beschleunigungsarbeit/Kinetische Energie

$$
W_B = \frac{1}{2}m \cdot v^2 = E_{kin}
$$

## Horizontaler Wurf

*OHNE* Berücksichtigung des Luftwiderstandes.

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\t_h_v0_phi.png">

$t_F$: Fallzeit [$s$]
$$
h = \frac{1}{2}g \cdot t^2 => t_F = \sqrt{\frac{2h}{g}} \\
x_W = v_0 \cdot t_F \\
v = \sqrt{v_0^2 + v_Z^2} \\
\phi = tan^{-1}(\frac{v_z}{v_0})
$$

### Bezugssystem nach unten

Kann *generell* angewendet werden wenn Objekte *keine* Anfangsposition haben und nach *unten* fallen.

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\h_of_t.png">
$$
h(t) = \frac{1}{2} g t^2 \\
h(t) = v_0t + \frac{1}{2}gt^2 \\
v = \sqrt{2gh} \\
v = \sqrt{v_0^2 + 2gh}
$$
$$
h = \overline{v}t \\
t_F = \sqrt{\frac{2h}{g}}
$$



<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\v_of_t.png">
$$
v(t) = gt \\
v(t) = v_0 + gt
$$

### Bezugssystem nach oben

Kann *generell* angewendet werden wenn Objekte *eine* Anfangsposition haben und nach *unten* fallen.

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\z_of_t.png">

$z'$:  Position eines Objekts nach einer bestimmten Fallzeit.
$z''$: Position eines Objekts nach einer bestimmten Fallzeit, das eine Startgeschwindigkeit hat.
$$
z(t)' = z_0 - \frac{1}{2}gt^2 \\
z(t)'' = z_0 + v_0t - \frac{1}{2}gt^2 \\
v = \sqrt{2gh} \\
v = \sqrt{v_0^2 - 2gh}
$$
<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\v_of_t2.png">
$$
v(t) = -gt \\
v(t) = v_0 - gt
$$

## Kreisbewegung

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\angular_velocity.png">

$\omega$: Winkelgeschwindigkeit/Kreisfrequenz [$\frac{1}{s}$]
$v$: Bahngeschwindigkeit [$\frac{m}{s}$]
$r$: Bahnradius
$U$: Umfang [$m$]
$T$: Periodendauer [$s$]
$f$: Frequenz der Umdrehung [$\frac{1}{s}$/$Hz$]
$$
\omega = \frac{\Delta \phi}{\Delta t} = \frac{2 \pi}{T} = 2 \pi \cdot f \\
v = \frac{U}{T} = \frac{2 \pi \cdot r}{T} = \omega \cdot r \\
T = \frac{1}{f} \Rightarrow f = \frac{1}{T}
$$
<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\angular_force.png">

$a_z$: Anzugsbeschleunigung zum Zentrum [$m/s$]
$F_z$: Anzugskraft zum Zentrum (=$F_R$) [$N$]
$$
a_z = \frac{2\pi \cdot v}{T} = \omega \cdot v = \omega^2 \cdot r = \frac{v^2}{r} \\
\phi = \omega \cdot t \\
F_z = m \cdot a_z
$$

## Schwingungen

| Welle                                             | Stehende Welle                                               |              |
| ------------------------------------------------- | ------------------------------------------------------------ | ------------ |
| Wasserwelle<br />Elektromagnetische Welle (Licht) | Wasserwelle in Resonator<br />Licht in Laserresonator<br />feste Seilwelle | transversal  |
| Schallwelle                                       | Schallwelle in Resonator                                     | longitudinal |

Harmonische Schwingung ist gegeben wenn $F = -D \cdot y$.

### Harmonische Schwingung

$\hat{y}$ / $\hat{x}$: Amplitude [$m$]
$y$ / $x$: (momentane) Auslenkung [$m$]

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\harmonic_ossilation_sine_time.png">
$$
y = \hat{y} \cdot sin(\omega \cdot t) \\
\hat{v} = \omega \cdot \hat{y} \\
\hat{a} = \omega \cdot \hat{v} = \omega^2 \cdot \hat{y}
$$

### Lineare Welle

$k$: Wellenzahl [$\frac{1}{m}$]
$v$ / $c$: Ausbreitungsgeschwindigkeit [$\frac{m}{s}$]
$\lambda$: Wellenlänge [$m$]

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\harmonic_ossilation_sine_distance.png">
$$
k = \frac{2 \cdot \pi}{\lambda} \\
y = \hat{y} \cdot sin(\omega \cdot t \pm k \cdot x) \\
c = \frac{\lambda}{T} = \lambda \cdot f
$$
Der Operand $\pm$  kann geändert werden je nachdem in welche Richtung sich die Welle im Koordinatensystem ausbreitet. $-$ für rechts oder ins positive $x$ und $+$ für links oder ins negative $x$.

### Feder & Pendel

$m$: Masse des schwingenden Körpers [$kg$]
$D$: Federkonstante [$\frac{N}{m}$]
$l$: Pendellänge [$m$]
$$
T = 2\pi\sqrt{\frac{m}{D}} \\
T = 2\pi\sqrt{\frac{l}{g}}
$$

## Elektrizität

$Q$: Ladung [$C$ (Coulomb)]
$I$: Strom [$A$]
$U$: Spannung [$V$]
$P$: Leistung [$W$]
$$
1C = 6.24 \cdot 10^{18}e \\
I = \frac{\Delta Q}{\Delta t} \\
U = \frac{\Delta W}{\Delta Q} \\
P = U \cdot I = \frac{U^2}{R} = R \cdot I^2
$$

### Spezifischer Widerstand

$\sigma$: spezifische Leitfähigkeit []
$\rho$: spezifischer Widerstand [$\Omega \cdot m$ / $\Omega \cdot \frac{mm^2}{m}$]
$A$: Fläche Leiter [$m^2$]
$l$: Länge Leiter [$m$]
$$
I = \sigma \cdot \frac{A}{l} \cdot \Delta U \\
\Delta U = \frac{1}{\sigma} \cdot \frac{l}{A} \cdot I \\
\rho = \frac{1}{\sigma} \\
R = \rho \cdot \frac{l}{A}
$$

### Ohmsches Gesetz

$R$: Widerstand [$\Omega$]
$$
U = R \cdot I \Rightarrow R = \frac{U}{I}
$$

### Mehrere Widerstände

<img style="width: 50%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\electricity_serial_parallel.png">

*Seriell*:
$$
I = I_1 = I_2 \\
U = U_1 + U_2 \\
R = R_1 + R_2
$$
*Parallel*:
$$
I = I_1 + I_2 \\
U = U_1 = U_2 \\
R = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}}
$$

### Ungenauigkeiten durch Messgeräte

1. Schaltung: $I_1 \neq I$ weil $I_2 > 0$, für kleine Widerstände für $R$ geeignet
2. Schaltung: $U_2 \neq U$ weil $U_1 > 0$, für grosse Widerstände für $R$ geeignet

<img style="width: 50%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\electricity_measurement_inaccuracies.png">
$$
I_1 = I - I_2 = I - \frac{U}{R_V} \\
U_2 = U - U_1 = U - R_A \cdot I
$$

### Modell Spannungsquelle

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\electricity_internal_resistor.png">
$$
U_a = U_0 - \Delta U = U_0 - R_i \cdot I
$$


## Acknowledgements

Author(s): d20cay

Last updated: See [changelog](https://d20cay.com/changelog)