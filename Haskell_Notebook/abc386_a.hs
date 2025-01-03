import Data.Set qualified as Set

main::IO ()
main = do
    as<-words<$>getLine
    if (length.Set.fromList $ as) == 2
        then putStrLn "Yes"
        else putStrLn "No"