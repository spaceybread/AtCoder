import Data.List

main::IO()

main = do
    num <- getLine
    let s = group num
    print $ solve 0 s

solve::Int -> [String] -> Int
solve n[] = n
solve n(x:xs)
    | head x == '0' = solve (n + m `div` 2 + if even m then 0 else 1) xs
    | otherwise     = solve (n + m) xs
    where m = length x