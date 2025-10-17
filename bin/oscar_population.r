####################
### Oscart Population Age and Gender Distribution 
####################


library(dplyr)   
library(ggplot2)


df <- data.frame(Gender = rep(c("M", "F"), each = 20),
                 Age = rep(c("0-10", "11-20", "21-30", "31-40", "41-50",
                           "51-60", "61-70", "71-80", "81-90", "91-100"), 4),                 
                 Value = sample(seq(50, 100, 5), 40, replace = TRUE)) %>%
  mutate(Value = ifelse(Gender == "F", Value *-1 , Value))

print(df)

df_dengen <- read.table("/mnt/oscar_dream_dgm/data/oscar_population_age_gender",sep="\t",header=T)

ggplot(df_dengen) +
geom_col(aes(fill = Gender,
            y = Value,
            x = Age), 
        position = "dodge") + 
scale_y_continuous(labels = abs,
                    expand = c(0, 0)) +
#scale_fill_manual(values = hcl(h = c(15,195,15,195),
#                                c = 100,
#                                l = 65,
#                                alpha=c(0.4,0.4,1,1)),
#                name = "") +
coord_flip() +
facet_wrap(.~ Gender, 
            scale = "free_x",
            strip.position = "bottom") +
theme_minimal() +
theme(legend.position = "bottom",
    panel.spacing.x = unit(0, "pt"), 
    strip.background = element_rect(colour = "black"))

ggsave("oscar.png")
ggsave("oscar.pdf")