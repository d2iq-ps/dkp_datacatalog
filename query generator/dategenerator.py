for year in range(2017, 2022):
    for month in range(1, 12):
        next_month = month + 1
        month = str(month)
        next_month = str(next_month)
        if len(month) == 1:
            month = "0"+month
        if len(next_month) == 1:
            next_month = "0"+next_month
        print(f"https://api.gdeltproject.org/api/v2/doc/doc?query=kubernetes&mode=ArtList&maxrecords=250&sort=DateAsc&format=json&STARTDATETIME={year}{month}01000000&ENDDATETIME={year}{month}31235959")
