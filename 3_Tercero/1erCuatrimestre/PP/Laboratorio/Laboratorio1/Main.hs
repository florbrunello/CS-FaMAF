module Main (main) where

import Data.Maybe (fromMaybe)
import System.Console.GetOpt (ArgDescr(..), ArgOrder(..), OptDescr(..), getOpt)
import System.Directory (listDirectory)
import System.Environment (getArgs)
import Text.Read (readMaybe)

import Interp (Conf(name), initial)
import Dibujos.Ejemplo (ejemploConf)
import Dibujos.Feo (feoConf)
import Grilla (grillaConf)
import Dibujos.Escher (escherConf)

-- Lista de configuraciones de los dibujos
configs :: [Conf]
configs = [ejemploConf,feoConf,grillaConf,escherConf]


-- Dibuja el dibujo n
initial' :: [Conf] -> String -> IO ()
initial' [] n = do
    putStrLn $ "No hay un dibujo llamado " ++ n
initial' (c : cs) n = 
    if n == name c then
        initial c 400
    else
        initial' cs n


main :: IO ()
main = do
  args <- getArgs
  if head args == "--lista" then do
    let dir = head $ tail args
    files <- listDirectory dir 
    print files
  else
    initial' configs $ head args
