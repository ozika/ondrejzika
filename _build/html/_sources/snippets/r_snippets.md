## Different useful snippets in R

### basic funcs

**standard error**

```r


```

### linear models

#### Generate mixed effect model equation
<script src="https://gist.github.com/ozika/f9045775a5cff21f69c7ef2336cd773d.js"></script>

### data manipulations

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

