
setwd("/Users/luka/Documents/GitRepos/psis2017.git/Project/Data")

weekSummry = read.csv2("ridersWeek.csv")

randomRows = function(df,n){
  return(df[sample(nrow(df),n),])
}

# enacba za izracun kulk dober je bil teden
# intensity * duration * hr (per week) / 7
summary(weekSummry)

# cleanup
weekSummry$mon_intensity = as.numeric(as.character(weekSummry$mon_intensity))
weekSummry$tue_intensity = as.numeric(as.character(weekSummry$tue_intensity))
weekSummry$wed_intensity = as.numeric(as.character(weekSummry$wed_intensity))
weekSummry$thu_intensity = as.numeric(as.character(weekSummry$thu_intensity))
weekSummry$fri_intensity = as.numeric(as.character(weekSummry$fri_intensity))
weekSummry$sat_intensity = as.numeric(as.character(weekSummry$sat_intensity))
weekSummry$sun_intensity = as.numeric(as.character(weekSummry$sun_intensity))

weekSummry$mon_duration = as.numeric(as.character(weekSummry$mon_duration))
weekSummry$tue_duration = as.numeric(as.character(weekSummry$tue_duration))
weekSummry$wed_duration = as.numeric(as.character(weekSummry$wed_duration))
weekSummry$thu_duration = as.numeric(as.character(weekSummry$thu_duration))
weekSummry$fri_duration = as.numeric(as.character(weekSummry$fri_duration))
weekSummry$sat_duration = as.numeric(as.character(weekSummry$sat_duration))
weekSummry$sun_duration = as.numeric(as.character(weekSummry$sun_duration))

weekSummry$mon_hr = as.numeric(as.character(weekSummry$mon_hr))
weekSummry$tue_hr = as.numeric(as.character(weekSummry$tue_hr))
weekSummry$wed_hr = as.numeric(as.character(weekSummry$wed_hr))
weekSummry$thu_hr = as.numeric(as.character(weekSummry$thu_hr))
weekSummry$fri_hr = as.numeric(as.character(weekSummry$fri_hr))
weekSummry$sat_hr = as.numeric(as.character(weekSummry$sat_hr))
weekSummry$sun_hr = as.numeric(as.character(weekSummry$sun_hr))

maxHr = mean( c( median(weekSummry$mon_hr), median(weekSummry$tue_hr), median(weekSummry$wed_hr), median(weekSummry$thu_hr), median(weekSummry$fri_hr), median(weekSummry$sat_hr), median(weekSummry$sun_hr) ))
maxDuration = mean( c( median(weekSummry$mon_duration), median(weekSummry$tue_duration), median(weekSummry$wed_duration), median(weekSummry$thu_duration), median(weekSummry$fri_duration), median(weekSummry$sat_duration), median(weekSummry$sun_duration) ))

weekSummry$weekIntensity = (weekSummry$mon_intensity + weekSummry$tue_intensity + weekSummry$wed_intensity + weekSummry$thu_intensity + weekSummry$fri_intensity + weekSummry$sat_intensity + weekSummry$sun_intensity) / 7 / 2
weekSummry$weekDuration = (weekSummry$mon_duration/maxDuration + weekSummry$tue_duration/maxDuration + weekSummry$wed_duration/maxDuration + weekSummry$thu_duration/maxDuration + weekSummry$fri_duration/maxDuration + weekSummry$sat_duration/maxDuration + weekSummry$sun_duration/maxDuration) / 7
weekSummry$weekHearthrate = (weekSummry$mon_hr + weekSummry$tue_hr + weekSummry$wed_hr + weekSummry$thu_hr + weekSummry$fri_hr + weekSummry$sat_hr + weekSummry$sun_hr) / 7 / maxHr
weekSummry$weekOveral = weekSummry$weekIntensity + weekSummry$weekDuration + weekSummry$weekHearthrate
medAthlete = median(weekSummry$weekOveral)
weekSummry$bestAtlethes[weekSummry$weekOveral > medAthlete] = "good"
weekSummry$bestAtlethes[weekSummry$weekOveral <= medAthlete] = "bad"

weekSummry
plot(weekSummry$weekOveral)

library(lattice)
xyplot(weekSummry$weekDuration~weekSummry$weekHearthrate, 
       col = c("blue", "red"),
       auto.key = list(TRUE, col = c("blue", "red")),
       groups = factor(weekSummry$bestAtlethes))

write.csv2(weekSummry, file = "classifiedRidersWeek.csv")

# create training sets
bestAthletesTrainingSet = weekSummry[weekSummry$weekOveral > medAthlete,]
write.csv2(bestAthletesTrainingSet, file = "bestAthletes_train.csv")
bestAthletesTestSet = randomRows(bestAthletesTrainingSet, 50)
bestAthletesTestSet1 = randomRows(weekSummry[weekSummry$weekOveral < medAthlete,], 250)
bestAthletesTestSetMerge = merge(bestAthletesTestSet, bestAthletesTestSet1, all = TRUE)
write.csv2(bestAthletesTestSetMerge, file = "bestAthletes_test.csv")

# create random test pool
randomTrainDF = randomRows(weekSummry, 400)
write.csv2(randomTestDF, file = "week_riders_random_train.csv")
randomTestDF = randomRows(weekSummry, 400)
write.csv2(randomTestDF, file = "week_riders_random_test.csv")

# trainig set without rider 1 and 2
bestAthletesTrainingSet$Rider = as.character(bestAthletesTrainingSet$Rider)
trainingSetWithoutR1R2 = bestAthletesTrainingSet[bestAthletesTrainingSet$Rider != "Rider1",]
trainingSetWithoutR1R2 = bestAthletesTrainingSet[bestAthletesTrainingSet$Rider != "Rider2",]
trainingSetWithoutR1R2 = bestAthletesTrainingSet[bestAthletesTrainingSet$Rider != "Rider3",]
write.csv2(trainingSetWithoutR1R2, file = "best_athletes_witout_r1_r2_r3_train.csv")
testSetWitoutR1R2 = randomRows(bestAthletesTrainingSet[bestAthletesTrainingSet$Rider == "Rider1",], 10)
testSetWitoutR1R2 = merge(testSetWitoutR1R2, randomRows(bestAthletesTrainingSet[bestAthletesTrainingSet$Rider == "Rider2",], 10), all = TRUE)
testSetWitoutR1R2 = merge(testSetWitoutR1R2, randomRows(bestAthletesTrainingSet[bestAthletesTrainingSet$Rider == "Rider3",], 20), all = TRUE)
testSetWitoutR1R2 = merge(testSetWitoutR1R2, randomRows(weekSummry[weekSummry$weekOveral < medAthlete,], 20), all = TRUE)
write.csv2(trainingSetWithoutR1R2, file = "best_athletes_witout_r1_r2_r3_test.csv")
