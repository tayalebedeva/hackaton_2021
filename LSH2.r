c<-c(180,233)
png(file="My_plot.png",  width = 500, height = 500)

barplot(c, name.args = 'Water and Others', col = c(1,2),ylim=c(1,300))

dev.off()
