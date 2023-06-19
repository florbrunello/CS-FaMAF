module Interp (
    interp,
    Conf(..),
    interpConf,
    initial
) where


import Graphics.Gloss(Picture, Display(InWindow), makeColorI, color, pictures, translate, white, display, Vector)
import Dibujo (Dibujo, foldDib)
import FloatingPic (FloatingPic, Output, grid, half, zero)
import qualified Graphics.Gloss.Data.Point.Arithmetic as V

-- Interpretación de un dibujo
interpRotar  :: FloatingPic -> FloatingPic
interpRotar f x w h = f (x V.+ w) h (zero V.- w)

interpEspejar :: FloatingPic -> FloatingPic
interpEspejar f x w h = f (x V.+ w) (zero V.- w) h

interpRotar45 :: FloatingPic -> FloatingPic
interpRotar45 f x w h = f (x V.+ half(w V.+ h)) (half(w V.+ h)) (half(h V.- w))

interpJuntar :: Float -> Float -> FloatingPic -> FloatingPic -> FloatingPic
interpJuntar n m f g x w h = pictures [f x (r V.* w) h, g (x V.+ (r V.* w)) (r' V.* w) h] where r' = n/(m+n) ; r = m/(m+n) 

interpApilar :: Float -> Float -> FloatingPic -> FloatingPic -> FloatingPic
interpApilar n m f g x w h = pictures [f (x V.+ (r' V.* h)) w (r V.* h), g x w (r' V.* h)] where r' = n/(m+n) ; r = m/(m+n) 

interpEncimar :: FloatingPic -> FloatingPic -> FloatingPic
interpEncimar f g x w h = pictures [f x w h, g x w h]

interp :: Output a -> Output (Dibujo a)
interp f = foldDib f interpRotar  interpRotar45 interpEspejar interpApilar interpJuntar interpEncimar

-- Configuración de la interpretación
data Conf = Conf {
        name :: String,
        pic :: FloatingPic
    }

interpConf :: Conf -> Float -> Float -> Picture
interpConf (Conf _ p) x y = p (0, 0) (x,0) (0,y)

-- Dada una computación que construye una configuración, mostramos por
-- pantalla la figura de la misma de acuerdo a la interpretación para
-- las figuras básicas. Permitimos una computación para poder leer
-- archivos, tomar argumentos, etc.
initial :: Conf -> Float -> IO ()
initial cfg size = do
    let n = name cfg
        win = InWindow n (ceiling size, ceiling size) (0, 0)
    display win white $ withGrid (interpConf cfg size size) size size
  where withGrid p x y = translate (-size/2) (-size/2) $ pictures [p, color grey $ grid (ceiling $ size / 10) (0, 0) x 10]
        grey = makeColorI 120 120 120 120