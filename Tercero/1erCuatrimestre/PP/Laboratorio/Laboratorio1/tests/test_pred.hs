import Test.HUnit
import Pred
import Dibujo

-- Test cambiar 
test_cambiar_1 = TestCase $ assertEqual "cambiar" (cambiar (== 1) (const (figura 1)) (figura 1)) (figura 1)
test_cambiar_2 = TestCase $ assertEqual "cambiar" (cambiar (== 1) (const (figura 1)) (figura 2)) (figura 2)
test_cambiar_3 = TestCase $ assertEqual "cambiar" (cambiar (== 1) (const (figura 1)) (juntar 1.0 1.0 (figura 1) (figura 2))) (juntar 1.0 1.0 (figura 1) (figura 2))
test_cambiar_4 = TestCase $ assertEqual "cambiar" (cambiar (== 1) (const (figura 2)) (juntar 1.0 1.0 (figura 1) (figura 2))) (juntar 1.0 1.0 (figura 2) (figura 2))

-- Test anyDib
test_anyDib_1 = TestCase $ assertEqual "anyDib" (anyDib (== 1) (figura 1)) True
test_anyDib_2 = TestCase $ assertEqual "anyDib" (anyDib (== 1) (figura 2)) False
test_anyDib_3 = TestCase $ assertEqual "anyDib" (anyDib (== 1) (juntar 1.0 1.0 (figura 1) (figura 1))) True
test_anyDib_4 = TestCase $ assertEqual "anyDib" (anyDib (== 1) (juntar 1.0 1.0 (figura 2) (figura 3))) False

-- Test allDib
test_allDib_1 = TestCase $ assertEqual "allDib" (allDib (== 1) (figura 1)) True
test_allDib_2 = TestCase $ assertEqual "allDib" (allDib (== 1) (figura 2)) False
test_allDib_3 = TestCase $ assertEqual "allDib" (allDib (== 1) (juntar 1.0 1.0 (figura 1) (figura 1))) True
test_allDib_4 = TestCase $ assertEqual "allDib" (allDib (== 1) (juntar 1.0 1.0 (figura 1) (figura 2))) False

-- Test andP
test_andP_1 = TestCase $ assertEqual "andP" (andP (== 1) (== 1) 1) True
test_andP_2 = TestCase $ assertEqual "andP" (andP (== 1) (== 2) 1) False

-- Test orP
test_orP_1 = TestCase $ assertEqual "orP" (orP (== 1) (== 2) 1) True
test_orP_2 = TestCase $ assertEqual "orP" (orP (== 1) (== 2) 3) False

tests :: Test
tests = TestList [test_cambiar_1, test_cambiar_2, test_cambiar_3, test_cambiar_4, test_anyDib_1, test_anyDib_2, test_anyDib_3, test_anyDib_4, test_allDib_1, test_allDib_2, test_allDib_3, test_allDib_4, test_andP_1, test_andP_2, test_orP_1, test_orP_2]

-- run the tests
main :: IO Counts
main = runTestTT tests
