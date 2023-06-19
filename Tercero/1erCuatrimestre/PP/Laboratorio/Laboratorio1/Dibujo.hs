{-# LANGUAGE LambdaCase #-}
module Dibujo (
    Dibujo,
    figura, rotar, espejar, rot45, apilar, juntar, encimar, comp,
    r180, r270,
    (.-.), (///), (^^^),
    cuarteto, encimar4, ciclar,
    foldDib, mapDib,
    figuras
) where


{-
<Dibujo> ::= Figura <Fig> | Rotar <Dibujo> | Espejar <Dibujo> 
    | Rot45 <Dibujo>
    | Apilar <Float> <Float> <Dibujo> <Dibujo> 
    | Juntar <Float> <Float> <Dibujo> <Dibujo> 
    | Encimar <Dibujo> <Dibujo>
-}


data Dibujo a = Figura a| Rotar(Dibujo a) | Espejar(Dibujo a) | Rot45(Dibujo a) |
                Apilar Float Float (Dibujo a) (Dibujo a)  | Juntar Float Float (Dibujo a) (Dibujo a) |
                Encimar (Dibujo a) (Dibujo a)
                deriving (Eq, Show)


-- Construcción de dibujo (abstraen los constructores)
rotar :: Dibujo a -> Dibujo a
rotar = Rotar

espejar :: Dibujo a -> Dibujo a
espejar = Espejar

rot45 :: Dibujo a -> Dibujo a
rot45  = Rot45

apilar :: Float -> Float -> Dibujo a -> Dibujo a -> Dibujo a
apilar = Apilar

juntar :: Float -> Float -> Dibujo a -> Dibujo a -> Dibujo a
juntar = Juntar

encimar :: Dibujo a -> Dibujo a -> Dibujo a
encimar = Encimar


-- Combinadores
-- Composición n-veces de una función con sí misma. Componer 0 veces
-- es la función constante, componer 1 vez es aplicar la función 1 vez, etc.
-- Componer negativamente es un error!
comp :: (a -> a) -> Int -> a -> a
comp f 1 = f
comp f n = f . (comp f (n-1))

-- Rotaciones de múltiplos de 90.
r180 :: Dibujo a -> Dibujo a
r180 = comp rotar 2

r270 :: Dibujo a -> Dibujo a
r270 = comp rotar 3

-- Pone una figura sobre la otra, ambas ocupan el mismo espacio.
(.-.) :: Dibujo a -> Dibujo a -> Dibujo a
(.-.) = apilar 1.0 1.0

-- Pone una figura al lado de la otra, ambas ocupan el mismo espacio.
(///) :: Dibujo a -> Dibujo a -> Dibujo a
(///) = juntar 1.0 1.0

-- Superpone una figura con otra.
(^^^) :: Dibujo a -> Dibujo a -> Dibujo a
(^^^) = encimar

-- Dadas cuatro figuras las ubica en los cuatro cuadrantes.
cuarteto :: Dibujo a -> Dibujo a -> Dibujo a -> Dibujo a -> Dibujo a
cuarteto d1 d2 d3 d4 = (.-.) ((///) d1 d2) ((///) d3 d4)

-- Una figura repetida con las cuatro rotaciones, superpuestas.
encimar4 :: Dibujo a -> Dibujo a
encimar4 d = (^^^) ((^^^) d (rotar d)) ((^^^) (r180 d) (r270 d))

-- Cuadrado con la misma figura rotada i * 90, para i ∈ {0, ..., 3}.
ciclar :: Dibujo a -> Dibujo a
ciclar a = cuarteto (rotar a) a (r180 a) (r270 a)

--Esquema para la manipulación de figuras básicas
figura :: a -> Dibujo a
figura = Figura

{-- Estructura general para la semántica-}
foldDib :: (a -> b) -> (b -> b) -> (b -> b) -> (b -> b) ->(Float -> Float -> b -> b -> b) 
           -> (Float -> Float -> b -> b -> b) -> (b -> b -> b) -> Dibujo a -> b
foldDib fun a b c d e f (Figura x) = fun x
foldDib fun a b c d e f (Rotar x)  = a (foldDib fun a b c d e f x)
foldDib fun a b c d e f (Rot45 x)  = b (foldDib fun a b c d e f x)
foldDib fun a b c d e f (Espejar x)= c (foldDib fun a b c d e f x)
foldDib fun a b c d e f (Apilar n1 n2 x y) = d n1 n2 (foldDib fun a b c d e f x) (foldDib fun a b c d e f y)
foldDib fun a b c d e f (Juntar n1 n2 x y) = e n1 n2 (foldDib fun a b c d e f x) (foldDib fun a b c d e f y)
foldDib fun a b c d e f (Encimar x y) = f (foldDib fun a b c d e f x) (foldDib fun a b c d e f y)

mapDib :: (a -> Dibujo b) -> Dibujo a -> Dibujo b
mapDib fun (Figura x)  = fun x
mapDib fun (Rotar x)   = Rotar (mapDib fun x)
mapDib fun (Espejar x) = Espejar (mapDib fun x)
mapDib fun (Rot45 x)   = Rot45 (mapDib fun  x)
mapDib fun (Encimar x y) = Encimar (mapDib fun x) (mapDib fun y)
mapDib fun (Apilar a b x y) = Apilar a b (mapDib fun x) (mapDib fun y)
mapDib fun (Juntar a b x y) = Juntar a b (mapDib fun x) (mapDib fun y)

-- Extrae todas las figuras básicas de un dibujo.
figuras :: Dibujo a -> [a]
figuras (Figura x)  = [x]
figuras (Rotar x)   = figuras x
figuras (Rot45 x)   = figuras x
figuras (Espejar x) = figuras x
figuras (Encimar x y) = figuras x ++ figuras y
figuras (Juntar w z x y) = figuras  x ++ figuras y
figuras (Apilar w z x y) = figuras x ++ figuras y