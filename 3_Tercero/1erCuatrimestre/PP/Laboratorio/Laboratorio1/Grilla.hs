module Grilla (
    grillaConf,
    grilla
) where

import Dibujo (Dibujo, juntar, apilar,figura)
import Graphics.Gloss(Picture, Display(InWindow), pictures, translate, Vector, text,scale)

import FloatingPic (Output)
import Interp (Conf(..), interp,interpConf)

row :: [Dibujo a] -> Dibujo a
row [] = error "row: no puede ser vacío"
row [d] = d
row (d:ds) = juntar (fromIntegral $ length ds) 1 d (row ds)

column :: [Dibujo a] -> Dibujo a
column [] = error "column: no puede ser vacío"
column [d] = d
column (d:ds) = apilar (fromIntegral $ length ds) 1 d (column ds)

grilla :: [[Dibujo a]] -> Dibujo a
grilla = column . map row

--Dados i j, crea un dibujo de un par (i,j)
parDib :: Int -> Int -> Dibujo (Int, Int)
parDib  i j = figura (i,j)

--Crea una grilla de pares (i,j)
parGrilla :: Dibujo (Int, Int)
parGrilla = grilla [map (parDib i) [0..7] | i <- [0..7]]

--Interpretación del par (i,j)
interpPar :: Output (Int, Int)
interpPar (i,j) x w h  = translate (fromIntegral j + fst x) (-(fromIntegral i*fst h) + snd x ) 
                        $ scale 0.1 0.1 $ text $ show (i,j)


grillaConf:: Conf
grillaConf = Conf {
    name = "Grilla",
    pic = interp interpPar parGrilla
}