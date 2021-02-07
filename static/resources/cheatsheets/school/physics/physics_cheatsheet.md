# Physik Cheatsheet

[TOC]

## Wärme

$Q$: Wärmeenergie [$J$]
$$
\Delta Q = m c \cdot \Delta T
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

### <img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\friction.png">

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

$a_z$: Anzugsbeschleunigung zum Zentrum
$F_z$: Anzugskraft zum Zentrum (=$F_R$)
$$
a_z = \frac{2\pi \cdot v}{T} = \omega \cdot v = \omega^2 \cdot r = \frac{v^2}{r} \\
\phi = \omega \cdot t \\
F_z = m \cdot a_z
$$

## Schwingungen

### Harmonische Schwingungen

$\hat{y}$ / $\hat{x}$: Amplitude
$y$ / $x$: (momentane) Auslenkung

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\harmonic_ossilation_sine_time.png">
$$
y = \hat{y} \cdot sin(\omega \cdot t) \\
\hat{v} = \omega \cdot \hat{y} \\
\hat{a} = \omega \cdot \hat{v} = \omega^2 \cdot \hat{y}
$$

$k$: Wellenzahl
$v$ / $c$: Ausbreitungsgeschwindigkeit
$\lambda$: Wellenlänge

<img style="width: 30%;" src="D:\MEGA\_edu\bms\physics\cheatsheet\harmonic_ossilation_sine_distance.png">
$$
k = \frac{2 \cdot \pi}{\lambda} \\
y = \hat{y} \cdot sin(k \cdot x) \\
c = \hat{y} \cdot sin(\omega \cdot t \pm k \cdot x) = \frac{\lambda}{T} = \lambda \cdot f
$$
Der Operand $\pm$  kann geändert werden je nachdem in welche Richtung sich die Welle im Koordinatensystem ausbreitet. $-$ für rechts oder ins positive $x$ und $+$ für links oder ins negative $x$.

### Federpendel

$$
T = 2\pi\sqrt{\frac{m}{D}} \\
T = 2\pi\sqrt{\frac{l}{g}}
$$

## Acknowledgements

Author(s): d20cay

Last updated: See [changelog](https://d20cay.com/changelog)