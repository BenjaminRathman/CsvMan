import initcsv
import csvedit



def main():
    S1L2Sorted = initcsv.CsvFile("S1L2Sorted")
    SS1League = initcsv.CsvFile("SS1League")
    csvedit.filter_rows_by_multiple_values(SS1League.filepath, S1L2Sorted.filepath,"AwayTeamId",["2","10","17","18","21","24"])


main()