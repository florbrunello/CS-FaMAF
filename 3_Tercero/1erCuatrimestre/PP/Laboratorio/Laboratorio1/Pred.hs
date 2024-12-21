module Pred (
  Pred,
  cambiar, allDib, orP, andP, anyDib
) where

import Dibujo

type Pred a = a -> Bool

-- Dado un predicado sobre básicas, cambia todas las que satisfacen
-- el predicado por la figura básica indicada por el segundo argumento.
cambiar :: Pred a -> (a -> Dibujo a) -> Dibujo a -> Dibujo a
cambiar pred f = mapDib (\x -> if pred x then f x else figura x)

-- Alguna básica satisface el predicado.
anyDib :: Pred a -> Dibujo a -> Bool
anyDib pred = foldDib pred id id id (\_ _ -> (||)) (\_ _ -> (||)) (||)

-- Todas las básicas satisfacen el predicado.
allDib :: Pred a -> Dibujo a -> Bool
allDib pred = foldDib pred id id id (\_ _ -> (&&)) (\_ _ -> (&&)) (&&)

-- Los dos predicados se cumplen para el elemento recibido.
andP :: Pred a -> Pred a -> Pred a
andP pred1 pred2 x = pred1 x && pred2 x

-- Algún predicado se cumple para el elemento recibido.
orP :: Pred a -> Pred a -> Pred a
orP pred1 pred2 x = pred1 x || pred2 x