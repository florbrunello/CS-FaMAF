module Dibujos.Escher (
    interpBasEscher,
    escherConf
) where

import Graphics.Gloss (white, line, polygon, pictures)
import qualified Graphics.Gloss.Data.Point.Arithmetic as V
import Dibujo (Dibujo, figura, juntar, rot45, cuarteto, encimar, espejar, apilar, rotar, r270, r180, (.-.), (///))
import FloatingPic (Output, half, zero, vacia)
import Interp (Conf(..), interp)

-- Supongamos que eligen.
type Escher = Bool

interpBasEscher :: Output Escher
interpBasEscher True a b c = pictures [line $ triangulo a b c, cara a b c]
  where
      triangulo a b c = map (a V.+) [zero, c, b, zero]
      cara a b c = polygon $ triangulo (a V.+ half c) (half b) (half c)
interpBasEscher False a b c = vacia a b c

-- El dibujo u.
dibujoU :: Dibujo Escher -> Dibujo Escher
dibujoU d = encimar 
                    (encimar d' (rotar d'))
                    (encimar (r180 d') (r270 d'))
            where d' = espejar $ rot45 d

-- El dibujo t.
dibujoT :: Dibujo Escher -> Dibujo Escher
dibujoT d = encimar 
                    d
                    (encimar d' (r270 d'))
            where d' = espejar $ rot45 d
    
-- Esquina con nivel de detalle en base a la figura p.
esquina :: Int -> Dibujo Escher -> Dibujo Escher
esquina 0 _ = figura False
esquina n d = cuarteto (esquina (n-1) d) (lado (n-1) d) (rotar (lado (n-1) d)) (dibujoU d)

-- Lado con nivel de detalle.
lado :: Int -> Dibujo Escher -> Dibujo Escher
lado 0 _ = figura False
lado n d = cuarteto (lado (n-1) d) (lado (n-1) d) (rotar d') d'
           where d' = dibujoT d


-- Por suerte no tenemos que poner el tipo!
noneto p q r s t u v w x = apilar 2 1 (juntar 2 1 p ((///) q r))
                                          ((.-.) (juntar 2 1 s ((///) t u)) 
                                                 (juntar 2 1 v ((///) w x)))

-- El dibujo de Escher:
escher :: Int -> Escher -> Dibujo Escher
escher n True = noneto 
                       (esquina n (figura True)) (lado n (figura True)) (r270 $ esquina n (figura True)) 
                       (rotar $ lado n (figura True)) (dibujoU (figura True)) (r270 $ lado n (figura True))
                       (rotar $ esquina n (figura True)) (r180 $ lado n (figura True)) (r180 $ esquina n (figura True))

escherConf :: Conf
escherConf= Conf{
    name="Escher",
    pic = interp interpBasEscher (escher 5 True)
}  