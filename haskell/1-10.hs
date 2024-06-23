import Data.List

main = undefined

-- sum of all even numbers below 1000 that are multiples of 3&5
p1 :: Int -> Int
p1 n = case n >= 1000 of
                True  -> 0
                False -> if (n `mod` 3 == 0 || n `mod` 5 == 0) then n + p1 (n + 1) else p1 (n+1)


fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib' (n-2) 0 1
    where
    fib' 0 x y = x+y
    fib' i x y = fib'(i-1) y (x+y)

-- sum of even fibs below 4 mil
p2 :: Int -> Int
p2 n = if fibn >= 4000000 then 0 else case (fibn `mod` 2) of
                                        1 -> p2 (n + 1)
                                        0 -> fibn + p2 (n + 1)
                                    where fibn = fib n

-- find largest prime factor of 600851475143
p3 :: Int -> Int -> [Int]
p3 1 _ = []
p3 2 _ = [2]
p3 n f = if (n `mod` f) == 0 then [f] ++ p3 (n `div` f) f else p3 n (f + 1)

-- largest palindromic number formed by multiplying two 3 digit integers together
p4 :: Int
p4 = head $ reverse $ sort [i*j | i <- [100..999], j <- [100..999], (reverse $ show (i*j)) == show(i*j)]


isDivisible :: Int -> Bool
isDivisible n = (length $ [i | i <- [1..20], (n `mod` i == 0)]) == 20

p5 :: [Int]
p5 = [i | i <- [20,40..1000000000], isDivisible i]

