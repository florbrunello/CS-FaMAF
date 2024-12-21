import Test.HUnit
import Dibujo

-- Test rotar
test_rotar_1 = TestCase (assertEqual "rotar" (rotar (figura 1)) (rotar (figura 1)))
test_rotar_2 = TestCase (assertEqual "rotar (rotar (figura 1))" (rotar (rotar (figura 1))) (rotar (rotar (figura 1))))

-- Test espejar
test_espejar_1 = TestCase (assertEqual "espejar" (espejar (figura 1)) (espejar (figura 1)))
test_espejar_2 = TestCase (assertEqual "espejar (espejar (figura 1))" (espejar (espejar (figura 1))) (espejar (espejar (figura 1))))

-- Test rot45
test_rot45_1 = TestCase (assertEqual "rot45" (rot45 (figura 1)) (rot45 (figura 1)))
test_rot45_2 = TestCase (assertEqual "rot45 (rot45 (figura 1))" (rot45 (rot45 (figura 1))) (rot45 (rot45 (figura 1))))

-- Test apilar
test_apilar = TestCase (assertEqual "apilar" (apilar 1 1 (figura 1) (figura 2)) (apilar 1 1 (figura 1) (figura 2)))

-- Test juntar
test_juntar = TestCase (assertEqual "juntar" (juntar 1 1 (figura 1) (figura 2)) (juntar 1 1 (figura 1) (figura 2)))

-- Test encimar
test_encimar = TestCase (assertEqual "encimar" (encimar (figura 1) (figura 2)) (encimar (figura 1) (figura 2)))

-- Test comp
test_comp = TestCase (assertEqual "comp suma" 4 (comp suma 3 1))
    where suma x = x + 1

-- Test r180
test_r180 = TestCase (assertEqual "r180 (figura 1)" (rotar (rotar (figura 1))) (r180 (figura 1)))

-- Test r270
test_r270 = TestCase (assertEqual "r270" (rotar (rotar (rotar (figura 1)))) (r270 (figura 1)))

-- Test (.-.)
test_comb_apilar = TestCase (assertEqual "(.-.)" (apilar 1.0 1.0 (figura 1) (figura 2)) ((.-.) (figura 1) (figura 2)))

-- Test (///)
test_comb_juntar = TestCase (assertEqual "(///)" (juntar 1.0 1.0 (figura 1) (figura 2)) ((///) (figura 1) (figura 2)))

-- Test (^^^)
test_comb_encimar = TestCase (assertEqual "(^^^)" (encimar (figura 1) (figura 2)) ((^^^) (figura 1) (figura 2)))

-- Test cuarteto
test_cuarteto = TestCase (assertEqual "cuarteto" (apilar 1.0 1.0 (juntar 1.0 1.0 (figura 1) (figura 2)) (juntar 1.0 1.0 (figura 3) (figura 4))) (cuarteto (figura 1) (figura 2) (figura 3) (figura 4)))

-- Test encimar4
test_encimar4 = TestCase (assertEqual "encimar4" (encimar (encimar (figura 1) (rotar (figura 1))) (encimar (rotar (rotar (figura 1))) (rotar (rotar (rotar (figura 1)))))) (encimar4 (figura 1)))

-- Test ciclar
test_ciclar = TestCase (assertEqual "ciclar" (apilar 1.0 1.0 (juntar 1.0 1.0 (rotar (figura 1)) (figura 1)) (juntar 1.0 1.0 (rotar (rotar (figura 1))) (rotar (rotar (rotar (figura 1)))))) (ciclar (figura 1)))

-- Test figura
test_figura = TestCase (assertEqual "figura" (figura 1) (figura 1))

-- Test foldDib
test_foldib_1 = TestCase (assertEqual "foldDib (figura 1)"            1 (foldDib id id id id (\_ _ a b -> a+b) (\_ _ a b -> a+b) (+) (figura 1)))
test_foldib_2 = TestCase (assertEqual "foldDib (rotar (figura 1))"    1 (foldDib id id id id (\_ _ a b -> a+b) (\_ _ a b -> a+b) (+) (rotar (figura 1))))
test_foldib_3 = TestCase (assertEqual "foldDib (espejar (figura 1))"  1 (foldDib id id id id (\_ _ a b -> a+b) (\_ _ a b -> a+b) (+) (espejar (figura 1))))
test_foldib_4 = TestCase (assertEqual "foldDib (rot45 (figura 1))"    1 (foldDib id id id id (\_ _ a b -> a+b) (\_ _ a b -> a+b) (+) (rot45 (figura 1))))
test_foldib_5 = TestCase (assertEqual "foldDib (juntar (figura 1))"   3 (foldDib id id id id (\_ _ a b -> a+b) (\_ _ a b -> a+b) (+) (juntar 1.0 1.0 (figura 1) (figura 2))))
test_foldib_6 = TestCase (assertEqual "foldDib (apilar (figura 1))"   3 (foldDib id id id id (\_ _ a b -> a+b) (\_ _ a b -> a+b) (+) (apilar 1.0 1.0 (figura 1) (figura 2))))
test_foldib_7 = TestCase (assertEqual "foldDib (encimar (figura 1))"  3 (foldDib id id id id (\_ _ a b -> a+b) (\_ _ a b -> a+b) (+) (encimar (figura 1) (figura 2))))

-- Test mapDib
test_mapdib_1 = TestCase (assertEqual "mapDib figura (figura 1)" (figura 1) (mapDib figura (figura 1)))
test_mapdib_2 = TestCase (assertEqual "mapDib figura (rotar (figura 1))" (rotar (figura 1)) (mapDib figura (rotar (figura 1))))
test_mapdib_3 = TestCase (assertEqual "mapDib figura (espejar (figura 1))" (espejar (figura 1)) (mapDib figura (espejar (figura 1))))
test_mapdib_4 = TestCase (assertEqual "mapDib figura (rot45 (figura 1))" (rot45 (figura 1)) (mapDib figura (rot45 (figura 1))))
test_mapdib_5 = TestCase (assertEqual "mapDib figura (juntar 1 1 (figura 1))" (juntar 1.0 1.0 (figura 2) (figura 4)) (mapDib (\a -> figura (a+a)) (juntar 1.0 1.0 (figura 1) (figura 2))))
test_mapdib_6 = TestCase (assertEqual "mapDib figura (apilar 1 1 (figura 1) (figura 2))" (apilar 1.0 1.0 (figura 2) (figura 4)) (mapDib (\a -> figura (a+a)) (apilar 1.0 1.0 (figura 1) (figura 2))))
test_mapdib_7 = TestCase (assertEqual "mapDib figura (encimar (figura 1) (figura 2))" (encimar (figura 2) (figura 4)) (mapDib (\a -> figura (a+a)) (encimar (figura 1) (figura 2))))

-- Test figuras
test_figuras_1 = TestCase (assertEqual "figuras (figura 1)" [1] (figuras (figura 1)))
test_figuras_2 = TestCase (assertEqual "figuras (rotar (figura 1))" [1] (figuras (rotar (figura 1))))
test_figuras_3 = TestCase (assertEqual "figuras (espejar (figura 1))" [1] (figuras (espejar (figura 1))))
test_figuras_4 = TestCase (assertEqual "figuras (rot45 (figura 1))" [1] (figuras (rot45 (figura 1))))
test_figuras_5 = TestCase (assertEqual "figuras (juntar 1.0 2.0 (figura 1) (figura 2))" [1,2] (figuras (juntar 1.0 2.0 (figura 1) (figura 2))))
test_figuras_6 = TestCase (assertEqual "figuras (apilar 1.0 2.0 (figura 1) (figura 2))" [1,2] (figuras (apilar 1.0 2.0 (figura 1) (figura 2))))
test_figuras_7 = TestCase (assertEqual "figuras (encimar (figura 1) (figura 2))" [1,2] (figuras (encimar (figura 1) (figura 2))))

tests :: Test
tests = TestList [test_rotar_1, test_rotar_2, test_espejar_1, test_espejar_2, test_rot45_1, test_rot45_2, test_apilar, test_juntar, test_encimar, test_comp, test_r180, test_r270, test_comb_apilar, test_comb_juntar, test_comb_encimar, test_cuarteto, test_encimar4, test_ciclar, test_figura, test_foldib_1, test_foldib_2, test_foldib_3, test_foldib_4, test_foldib_5, test_foldib_6, test_foldib_7, test_mapdib_1,test_mapdib_2, test_mapdib_3, test_mapdib_4, test_mapdib_5, test_mapdib_6, test_mapdib_7, test_figuras_1, test_figuras_2, test_figuras_3, test_figuras_4, test_figuras_5, test_figuras_6, test_figuras_7]

-- run the tests
main :: IO Counts
main = runTestTT tests