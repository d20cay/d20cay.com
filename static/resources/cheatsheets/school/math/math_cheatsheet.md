# Math Cheatsheet

[TOC]

## Umformungsregeln

$$
a^m \cdot a^n = a^{m+n} \\
\frac{a^m}{a^n} = a^{m-n} \\
a^n \cdot b^n = (a \cdot b)^n \\
\frac{a^n}{b^n} = (\frac{a}{b})^n \\
(a^n)^m = a^{n \cdot m} \\
\sqrt{a} = a^\frac{1}{2} \\~\\
lg(a \cdot b) = lg(a) + lg(b) \\
lg(\frac{a}{b}) = lg(a) - lg(b) \\
lg(a^b) = b \cdot lg(a) \\
a^{log_a(b)} = b
$$

## Trigonometry

Remember: *SOH CAH TOA*

### Sine

$$
\frac{a}{sin(\alpha)} = \frac{b}{sin(\beta)} = \frac{c}{sin(\gamma)}
$$

#### Right Angles

$$
sin(\theta) = \frac{o}{h} = \frac{opposite}{hypotenuse}
$$

### Cosine

$$
a^2 = b^2 + c^2 - 2bc \cdot cos(\alpha)\\
b^2 = a^2 + c^2 - 2ac \cdot cos(\beta)\\
c^2 = a^2 + b^2 - 2ab \cdot cos(\gamma)
$$

#### Right Angles

$$
cos(\theta) = \frac{a}{h} = \frac{adjacent}{hypotenuse}
$$

### Tangent

$$
tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}
$$

#### Right Angles

$$
tan(\theta) = \frac{o}{a} = \frac{opposite}{adjacent}
$$

## Geometry

### Similarity

$$
s = k \cdot s_0 \\
A = k^2 \cdot A_0 \\
V = k^3 \cdot V_0 \\
$$

### Triangle

#### Equilateral

$$
h = \frac{\sqrt{3}}{2}a \\
A = \frac{\sqrt{3}}{4}a^2
$$

#### Right Angle

$$
A = \frac{a \cdot b}{2}
$$

### Circle

$$
A = \pi \cdot r^2 \\
U = \pi \cdot 2r = \pi \cdot d
$$

### Pyramid

$$
V = \frac{G \cdot h}{3} \\
$$

### Tetrahedron

![tetraeder](D:\MEGA\_edu\bms\math\cheatsheet\tetraeder.png)
$$
V = \frac{\sqrt{2}}{12}a^3
$$

### Kegel

![kegel](D:\MEGA\_edu\bms\math\cheatsheet\kegel.png)

<img style="width: 30%;" src="D:\MEGA\_edu\bms\math\cheatsheet\kegel_mantel.png">
$$
V = \frac{G \cdot h}{3} = \frac{r^2\pi \cdot h}{3} \\
b = 2\pi \cdot r \\
M = \frac{b \cdot m}{2} = r\pi \cdot m \\
m = G + M \\~\\
m^2 = h^2 + r^2 \\
\alpha = 360^\circ \cdot \frac{r}{m}
$$

### Kugel

$$
V = \frac{4}{3}r^3\pi \\
A = 4\pi r^2
$$

## Vector Geometry

### Definition

$$
\vec{a} = \begin{pmatrix}a_x\\a_y\end{pmatrix} \\
\vec{a} = \begin{pmatrix}a_x\\a_y\\a_z\end{pmatrix} \\
$$

### Getting a Vector from Two Points

$$
B = (11;-2) \quad C = (8;6) \\~\\
\vec{BC} = \begin{pmatrix}C_x\\C_y\end{pmatrix} - \begin{pmatrix}B_x\\B_y\end{pmatrix}\\
$$

### Stretching

$$
k \cdot \vec{a}\\
k \cdot \begin{pmatrix}a_x\\a_y\end{pmatrix}\\
\begin{pmatrix}k \cdot a_x\\k \cdot a_y\end{pmatrix}\\
\begin{pmatrix}a'_x\\a'_y\end{pmatrix}
$$

### Linear Combination

AKA aligning the tip of each vector to the tail of another vector, resulting in a chain, which then gives you the starting point of the combination of vectors.
$$
\vec{x} = k_1\vec{a} + k_2\vec{b} + k_3\vec{c}
$$



### Linear Dependency

2 Vectors are linearly dependent if you can achieve one of the vectors by multiplying the other vector with any value of k, where k can't be 0.
$$
\vec{a} = k \cdot \vec{b}
$$
If there is a solution where $k_1$, $k_2$, $k_3$, ... are all != 0 then the three vectors are linearly dependent.
$$
\begin{pmatrix}0\\0\\0\end{pmatrix} = k_1 \cdot \vec{a} + k_2 \cdot \vec{b} + k_3 \cdot \vec{c}
$$

### Scalar Absolute Value (Length)

$$
\vert\vec{a}\vert = \sqrt{{a_x}^2 + {a_y}^2}\\
\vert\vec{b}\vert = \sqrt{{b_x}^2 + {b_y}^2 + {b_z}^2}\\
\vdots
$$

#### Unit vector

A unit vector is a vector that equals to 1 in its absolute value. The following formula can be used to determine the unit vector pointing in the same direction as the vector $a$.
$$
\vec{e}_a = \frac{1}{\vert\vec{a}\vert}*\vec{a} = \frac{\vec{a}}{\vert\vec{a}\vert}
$$

You can use the following formula to figure out what the new vector should be if it's to point in the same direction as the given one $a$ but have a specific length $l$.
$$
\vec{a}_l = \frac{l}{\vert\vec{a}\vert}*\vec{a}
$$

### Dot product

$$
\vec{a} \cdot \vec{b} = a_xb_x+a_yb_y\\
\vec{a} \cdot \vec{b} = a_xb_x+a_yb_y+a_zb_z\\
\vdots
$$

OR
$$
\vec{a} \cdot \vec{b} = cos(\alpha) \cdot \vert\vec{a}\vert \cdot \vert\vec{b}\vert\\
$$

The Scalar Absolute value can be calculated with the use of the `dotp` function using the TI-Nspire CX CAS as follows.

```python
function dotp(veca, vecb):
    return veca.x * vecb.x + veca.y * vecb.x


function dotp(veca, vecb):
    return veca.x * vecb.x + veca.y * vecb.y + veca.z * vecb.z
```

$$
\vert\vec{AB}\vert = \sqrt{dotp(\vec{AB}, \vec{AB})}
$$

### Angles

Vectors need to point ***AWAY*** from angle!
$$
\vec{AC} \cdot \vec{AB} = \cos(\alpha) \cdot \vert\vec{AC}\vert \cdot \vert\vec{AB}\vert\\
\cos(\alpha) = \frac{\vec{AC} \cdot \vec{AB}}{\vert\vec{AC}\vert \cdot \vert\vec{AB}\vert}\\
\alpha = \cos^{-1}(\frac{\vec{AC} \cdot \vec{AB}}{\vert\vec{AC}\vert \cdot \vert\vec{AB}\vert})
$$

### Vector Shadow

$$
\vert\vec{a_b}\vert = \vert\vec{a}\vert \cdot \cos(\alpha)\\
\vec{a_b} = \vert\vec{a_b}\vert \cdot \vec{e_b}\\
\vec{a_b} = \vert\vec{a}\vert \cdot \cos(\alpha) \cdot \vec{e_b}
$$

<img src="D:\MEGA\_edu\bms\math\cheatsheet\vector_shadows.png" style="width: 30%;">

### Straights

#### Parameter Definition

$$
g: \vec{r} = \vec{a} + t \cdot \vec{u}
$$

#### Positional Relationships

Two straights can be in one of four relations: *identical*, *intersecting in one point*, *parallel and non-intersecting*, *not parallel*. By defining both of the straights generally
$$
g: \vec{r} = \vec{a} + t \cdot \vec{u}\\
h: \vec{r} = \vec{b} + s \cdot \vec{v}
$$
we can make some determinations about when which of these cases are true.

If the equation $\vec{a} + t \cdot \vec{u} = \vec{b} + s \cdot \vec{v}$ has

1. one solution then *g* and *h* intersect in one point.
2. no solutions
   1. and $\vec{u} = k\vec{v}$ is valid the straights *g* and *h* are parallel.
   2. and $\vec{u} = k\vec{v}$ is invalid the straights *g* and *h* are not parallel.
3. infinite solutions then *g* and *h* are the same.

For straights in a 2D space the case 2.2 is not possible.

## Exponential functions

$$
E = S \cdot q^t
$$

You get the resulting value $E$ by multiplying the starting value $s$ with the result of the growth factor $q$ to the power of time $t$ that has passed. This can be more generally described as:
$$
f(x) = b \cdot a^x
$$

## Logistical functions

$$
f(t) = \frac{a \cdot S}{a + (S-a)e^{-kt}}
$$

Here $a$ is defined as the y-axis intercept of the function, or the starting value if you will. $S$ is defined as the value of $f(t)$ when $t$ is infinitely big or otherwise referred to as carrying capacity. This can be more generally described as (might be inaccurate as I can't find a concise formula from different sources):
$$
f(x) = \frac{a \cdot S}{a + (S-a)e^{-kx}}
$$

## Acknowledgements

Author(s): d20cay, (SirWJohnson)

Modified: 2020-11-30