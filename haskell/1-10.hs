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

--smallest number divisible by all numbers between 1 and 20
p5 :: [Int]
p5 = [i | i <- [20,40..1000000000], isDivisible i]

-- difference between square of sum and sum of squares of first 100
p6 :: Int
p6 = (sum [i | i <- [1..100]])^2 - sum [i^2 | i <- [1..100]]


isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral


factorize :: Int -> Int -> [Int]
factorize 1 _ = []
factorize 2 _ = [2]
factorize n f = if (n `mod` f) == 0 then [f] ++ factorize (n `div` f) f else factorize n (f+1)  

-- find 10001st prime number
p7 :: [Int]
p7 = [2] ++ [i | i <- [3..100000], (length $ (factorize i 2)) == 1]

thousand_digit_num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

substr :: Int -> Int -> [a] -> [a]
substr start end s = take (end - start) (drop start s)

getProd :: String -> Int
getProd "" = 1
getProd (x:xs) = ((read [x]) :: Int) * getProd xs

p8 :: Int
p8 = head $ reverse $ sort $ map (getProd) [substr i (i+13) thousand_digit_num | i <- [0..((length $ thousand_digit_num) - 13)]]