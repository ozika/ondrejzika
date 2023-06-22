## Different useful snippets in R

### Plotting

**Regression coefficients with `parameters` package**
Sometimes one wants to change the color of the plots, e.g. according to significance

<script src="https://gist.github.com/ozika/422d004618cb9b55e21c333341367213.js"></script>

### linear models

#### Generate mixed effect model equation
<script src="https://gist.github.com/ozika/f9045775a5cff21f69c7ef2336cd773d.js"></script>

### Data manipulations

Split continuous to categorical at specific breakponts

```r
tdf<- tdf %>% 
  mutate(
    wave = case_when(
        session < 6 ~ "first_wave",   
        session >= 6 & session < 14 ~ "summer_nowave", 
        session >= 14 ~ "second_wave"
        
    )
  )
```

### ggplot

