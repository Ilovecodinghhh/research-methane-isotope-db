
--- Page 1 ---
Global Fossil Methane Emissions Constrained by Multi‐
Isotopic Atmospheric Methane Histories
Ryo Fujita1,2
, Heather Graven1
, Giulia Zazzeri1,3, Benjamin Hmiel4,5, Vasilii V. Petrenko4
,
Andrew M. Smith6
, Sylvia E. Michel7, and Shinji Morimoto8
1Department of Physics, Imperial College London, London, UK, 2Meteorological Research Institute, Japan Meteorological
Agency, Tsukuba, Japan, 3Ricerca sul Sistema Energetico (RSE), Milan, Italy, 4Department of Earth and Environmental
Sciences, University of Rochester, Rochester, NY, USA, 5Environmental Defense Fund, New York, NY, USA, 6Centre for
Accelerator Science, Australian Nuclear Science and Technology Organisation (ANSTO), Lucas Heights, NSW, Australia,
7Institute of Arctic and Alpine Research, University of Colorado, Boulder, CO, USA, 8Center for Atmospheric and Oceanic
Studies, Graduate School of Science, Tohoku University, Sendai, Japan
Abstract The global CH4 budget of sources and sinks is highly uncertain, particularly the emissions from
specific sources such as fossil fuels (FF) or agriculture. Here, we estimate plausible global CH4 source and sink
scenarios using historical observations and simulations of atmospheric CH4 mole fraction and its stable isotopic
(δ13C‐CH4, δD‐CH4) and radiocarbon (Δ14C‐CH4) composition, combining constraints from all these tracers for
the first time. We employ a one‐box model along with a Monte Carlo particle filter technique, explicitly
exploring the impact of each isotopic constraints and uncertainties in prior CH4 source and sink parameters on
posterior sectorial source fractions. We find our posterior anthropogenic FF emissions at the global scale are
30% lower than previous isotope‐based studies. Our analysis suggests previous δ13C‐CH4‐based studies are
potentially biased because the current database‐derived estimate of the global mean biogenic δ13C‐CH4 source
signature is too low and/or current sink‐weighted total carbon kinetic isotope effect is underestimated. We find
modern atmospheric Δ14C‐CH4 data constrains lower global FF emissions after 1980s, which is contrary to the
most recent finding that utilized atmospheric Δ14C‐CH4 data, but supported by an independent estimate of
global nuclear 14CH4 emissions. Our multi‐isotopic constraints align with CH4‐only inversion results, while
reducing their uncertainties with greater robustness against different prior emission scenarios. We find strong
constraints not only on FF emissions but also other key sources and sinks, showing that long‐term multi‐isotopic
observations are critical for refining the global CH4 budget and developing effective CH4 emission mitigation
strategies.
Plain Language Summary Reduction of methane (CH4) emissions is a key element of climate
change mitigation. However, studies using different techniques to quantify emissions from specific sources
(e.g., fossil fuel (FF) or agriculture) are in conflict. Isotopic tracers are useful because different CH4 sources
have different isotopic signatures, especially radiocarbon for distinguishing between fossil and biogenic
sources, but most studies have not used all data available or accounted for all relevant uncertainties in
parameters related to the isotopic methane budget. Here, we synthesize all available constraints from
atmospheric CH4 concentration and its major isotopologues (13CH4, CH3D, and 14CH4) for 1750–2015,
considering the relevant uncertainties, to estimate global CH4 emissions and sinks. We find our global total
emissions from the FF industry are lower than other previous isotope‐based studies. Our study provides critical
constraints on the global CH4 emissions, which can support climate mitigation efforts, including the Global
Methane Pledge.
1. Introduction
Atmospheric CH4 concentration has more than doubled over the industrial era, with anthropogenic CH4 emissions
contributing ∼30% to anthropogenic greenhouse gas effective radiative forcing over 1750–2019 (IPCC, 2021),
while the CH4 growth rate has varied substantially in recent years with record high growth in 2020 and 2021
(Dlugokencky et al., 2021). The partitioning of CH4 sources and their contributions to CH4 growth rate variations
is an area of controversy and uncertainty, primarily because there is a wide range of poorly quantified anthro-
pogenic sources (e.g., agriculture, landfills, fossil fuels (FFs)), natural sources (e.g., wetlands, freshwater,
geological processes), and sinks (mainly chemical reactions with OH) (Saunois et al., 2020). The uncertainties in
RESEARCH ARTICLE
10.1029/2024JD041266
Key Points:
•
Bottom‐up estimates of natural CH4
emissions are too high, while bottom‐
up estimates of anthropogenic CH4
emissions are not too low
•
Our global total emissions from the
fossil fuel industry are 30% lower than
previous isotope‐based studies
•
Atmospheric Δ14C data constrain
lower anthropogenic fossil sources,
consistent with a data‐based estimate
for nuclear 14CH4 emissions
Supporting Information:
Supporting Information may be found in
the online version of this article.
Correspondence to:
R. Fujita,
ryo.fujita@mri-jma.go.jp
Citation:
Fujita, R., Graven, H., Zazzeri, G., Hmiel,
B., Petrenko, V. V., Smith, A. M., et al.
(2025). Global fossil methane emissions
constrained by multi‐isotopic atmospheric
methane histories. Journal of Geophysical
Research: Atmospheres, 130,
e2024JD041266. https://doi.org/10.1029/
2024JD041266
Received 2 APR 2024
Accepted 31 OCT 2024
© 2025. The Author(s).
This is an open access article under the
terms of the Creative Commons
Attribution License, which permits use,
distribution and reproduction in any
medium, provided the original work is
properly cited.
FUJITA ET AL.
1 of 25


--- Page 2 ---
the CH4 budget limit the creation of effective mitigation policies and the prediction of future CH4 radiative
forcing.
A key question is the attribution of total fossil sources (i.e., FF industries plus natural geologic seepage) versus
biogenic sources to the global CH4 budget. Several recent studies have indicated that CH4 emissions from the FF
industry could be underestimated by bottom‐up inventory estimates (e.g., Hmiel et al., 2020; Schwietzke
et al., 2016). Further, atmospheric measurements have detected underestimated fugitive CH4 emissions from FF
production regions (Alvarez et al., 2018), flaring sites (Plant et al., 2022), and some urban regions (Sargent
et al., 2021), as well as unexpected CH4 “superemitters” (Lauvaux et al., 2022). However, the global significance
of underestimated fugitive emissions is not yet clear.
Atmospheric isotopic analyses, which exploit differing isotopic source signatures in stable isotopes (13CH4 and
CH3D) and radiocarbon (14CH4), indicate the total fossil sources comprise 28%–33% of global emissions (Fujita
et al., 2020; Lan et al., 2021; Lassey, Lowe et al., 2007; Schwietzke et al., 2016), whereas the Global Carbon
Project (GCP) suggest only 21%–24% (Saunois et al., 2020). Radiocarbon is an excellent fossil CH4 tracer
because radioactive decay over millions of years removed 14CH4 in fossil CH4 (Lassey, Lowe et al., 2007). Ice
core and firn air atmospheric Δ14C‐CH4 data show that natural geological emissions are small (Hmiel
et al., 2020), suggesting that the vast majority of these extra fossil emissions are from the FF industry, whereas
bottom‐up estimates of natural geological emissions indicate they could comprise up to ∼40% of total fossil
emissions (Etiope & Schwietzke, 2019). Challenges with applying Δ14C‐CH4 data are that data are sparse and
recent atmospheric Δ14C‐CH4 is also influenced by uncertain nuclear power plant (NPP) emissions (Lassey,
Etheridge, et al., 2007; Lassey, Lowe et al., 2007). Stable isotopic approaches also exploit differences in isotopic
signatures of different sources, but suffer from significant uncertainty of the major isotopic source signatures as
well as OH variability and its kinetic isotope effect (KIE), leading to ambiguous source attributions (Lan
et al., 2021; Rigby et al., 2017; Turner et al., 2017). Two recent δ13C‐CH4 inversion studies agree that un-
certainties limit the application of δ13C‐CH4 measurements in CH4 source attribution, but come to different
conclusions: Thanwerdas et al. (2022) highlight the impact of uncertainties in δ13C‐CH4 source signatures on
sectorial source attributions, whereas Basu et al. (2022) suggest the uncertainties in KIEs are more important than
the δ13C‐CH4 source signatures.
Here, we synthesize all available constraints from atmospheric CH4, δ13C‐CH4, δD‐CH4, and Δ14C‐CH4 ob-
servations for the first time to estimate plausible global CH4 source and sink scenarios over 1750–2015. We
utilize a one‐box atmospheric model and a particle filter (PF) (or sequential Monte Carlo filter) approach (Doucet
et al., 2001; Kitagawa, 1996) to optimize global CH4 source and sink parameters. We derive posterior distri-
butions of the CH4 source strengths as well as their isotope source signatures, total CH4 loss rate, KIEs, biospheric
turnover time, and average NPP 14CH4 emissions factor by evaluating the simulations against historical global
observational target ranges. In this study, we chose a one‐box model over a 3D transport model, prioritizing
simplicity, computational cost, and transparency for the scope of this study. Our simple box model approach
enables us to utilize not only δ13C‐CH4, which is relatively well sampled globally, but also δD‐CH4 and Δ14C‐
CH4, whose spatiotemporal data coverage is still sparse and thus have not been incorporated into 3D model
inversions so far. By leveraging the cheap calculation cost, we perform large ensemble simulations (100,000
realizations per each prior emission scenario) as well as many sensitivity tests to explore the impact of individual
data constraints and individual uncertainties in CH4 source and sink parameters when deriving sectorial CH4
source emissions.
2. Methods
2.1. Model Description
We conduct numerous forward simulations of CH4, 13CH4, CH3D, and 14CH4 using a one‐box model with varying
parameters. Following Lassey, Etheridge, et al. (2007), simple global mass balance equations for total CH4,
13CH4, CH3D, and 14CH4 were prepared as follows:
dCATM
dt
= ∑
N
i=1
Esrc(i) −CATM
λtot
(1)
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
2 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 3 ---
d(CATMR13C ATM)
dt
= ∑
N
i=1
Esrc(i)R13C src(i) −
1
KIECλtot
CATMR13C ATM
(2)
d(CATMRD ATM)
dt
= ∑
N
i=1
Esrc(i)RD src(i) −
1
KIEDλtot
CATMRD ATM
(3)
d(CATMR14C ATM)
dt
= ∑
N
i=1
Esrc(i)R14C src(i) + ϕWPWR −((
1
KIEC)
2 1
λtot
+ 1
λr
) CATMR14C ATM
(4)
where CATM is the atmospheric burden of total CH4; R13C, RD, and R14C denote the absolute stable carbon,
hydrogen, and radiocarbon isotope ratios (i.e., 13CH4/total CH4, CH3D/total CH4, and 14CH4/total CH4),
respectively, of atmosphere (ATM) and respective source categories (src); E indicates the global CH4 emissions
of respective source categories; N is the number of source categories, equal to five, consisting of anthropogenic
biogenic (BIO), natural BIO, anthropogenic FF, geologic (GEO), and biomass burning (BB) sources; λ denotes
the atmospheric lifetime for total CH4 sink processes (tot) and radioactive decay (r); KIEC and KIED are the sink‐
weighted total KIEs for stable carbon and hydrogen isotopes, respectively; and ϕWPWR represents the direct NPP
14CH4 emissions where WPWR is the annual electrical power production by pressurized water reactors (PWR) and
ϕ is the 14CH4 emissions per annual electrical power production (i.e., NPP 14CH4 emission factor) (GBq/GWa).
The atmospheric 13CH4, CH3D, and 14CH4 are convertible to δ13C‐CH4, δD‐CH4, and Δ14C‐CH4, respectively
(Text S1 in Supporting Information S1).
We prepared three alternative a priori global CH4 emission scenarios for 1750–2015 using three different ant-
hropogenic emission inventories: Community Emissions Data System (CEDS) (Hoesly et al., 2018; prepared for
Coupled Model Intercomparison Project Phase 6 (CMIP6), v2017‐05‐18) and Emissions Database for Global
Atmospheric Research version 5.0 and 6.0 (EDGARv5 and EDGARv6) (Crippa et al., 2020, 2021). We used the
same a priori estimates of BB, natural BIO, and GEO CH4 sources in all scenarios (Table S2 in Supporting Inf-
ormation S1). For the CEDS scenario, we adopted the global sectorial anthropogenic CH4 emissions for CEDS for
1850–2014 (decadal until 1970 and yearly afterward). For the EDGAR scenarios, we reconstructed the historical
emissions using EDGAR‐HYDE v1.4 for 1890–1960 (decadal) (Olivier & Berdowski, 2001; van Aardenne
et al., 2001), and combined it with EDGARv5.0 or EDGARv6.0 for 1970–2015 (yearly). The a priori anthropo-
genic CH4 emissions in 1750 were specified from Lassey, Etheridge, et al. (2007) for each source category, the CH4
emissions for EDGAR in 1850 were specified by CEDS, and the CH4 emissions for CEDS in 2015 were specified
by Gidden et al. (2019). To keep the data consistency where annual data were unavailable, each source emission
was linearly interpolated using the adjacent available data. For BB CH4 emissions, the annual mean historical
global emission data set for CMIP6 (BB4CMIP) (van Marle et al., 2017) over 1750–2015 was used for all three
scenarios. We included residential, commercial, and other sectors (called “RCO” in CEDS or “1.a.d Other sectors”
in EDGAR) into anthropogenic FF emissions, assuming this combustion was from FFs. A sensitivity test was
performed to investigate the impact of this choice (RCOem; Table S3 in Supporting Information S1). Time‐
invariant a priori natural CH4 emissions (e.g., wetland, freshwater, and GEO) were taken from bottom‐up aver-
ages for 2000–2009 (Saunois et al., 2020) (Table S2 in Supporting Information S1). Sensitivity tests were also
performed for different a priori interannually varying natural wetland emission scenarios (IAWetBIOem; Table S3
in Supporting Information S1). Emissions from freshwater systems vary widely between bottom‐up and top‐down
estimates (134–284 Tg CH4 yr−1 vs. less than 30 Tg CH4 yr−1; Saunois et al., 2020); thus, a scenario excluding
freshwater emissions were also examined in a sensitivity test (NoFRESHem; Table S3 in Supporting Informa-
tion S1).
Our a priori atmospheric total CH4 lifetime is based on Prather et al. (2012) (9.1 ± 0.9 years), which is constrained
by atmospheric methyl chloroform (MCF) for tropospheric OH and literature‐based estimates for the other sinks
(i.e., soil oxidations, stratospheric losses, and tropospheric Cl). To consider the potential time evolutions of at-
mospheric OH into Prather et al., 2012's scenario, we applied an ensemble mean anomaly (relative to the 1998–
2007 mean) of global OH computed by Earth System Models (ESMs) that participated in the CMIP6 (Stevenson
et al., 2020) to the loss rate of tropospheric CH4‐OH reactions in Prather et al. (2012). The prior OH anomaly from
Stevenson et al. (2020) used in our base simulation shows little changes from 1850 to 1980, followed by strong
increases by 9% through 2014. In contrast, recent MCF‐based OH shows downward trends by about 8% since
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
3 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 4 ---
2005 (Rigby et al., 2017; Turner et al., 2017) or rather stable trends since 2000 (Naus et al., 2021; Patra
et al., 2021), the latter being consistent with the empirical reconstruction estimate (Nicely et al., 2018). We
therefore tested the sensitivity of different prior OH scenarios for the recent decades as time‐invariant or from
recent MCF‐based estimates (OHtrend; Table S3 in Supporting Information S1). Note that because we did not
explicitly simulate different loss processes in the model (see Equations 1–4), such time variations of tropospheric
OH need to be interpreted as those of total loss rates after the sink fractions in Prather et al. (2012) is applied.
The WPWR were taken from Lassey, Etheridge, et al. (2007) for 1960–1971 and assumed to be zero before 1960. For
1972–2015, the database of annual energy output for PWRs from International Atomic Energy Agency's Power
Reactor Information System (IAEA PRIS, 2017) was used. The absolute radiocarbon isotope ratio of biospheric
(i.e., BIO and BB) sources, R14C_bios, was calculated following Lassey, Etheridge, et al. (2007) as follows:
R14C bios(t) = ∫
∞
0
(1 + Δ14CO2(t −tʹ)/1000) F(tʹ) exp (−λrtʹ) dtʹ
(5)
F(tʹ) = exp (−tʹ/τbios)
τbios
(6)
where Δ14CO2 is the time series of atmospheric Δ14C‐CO2, F(t’) is an exponential distribution of lag times (i.e., the
residence time of the biospheric carbon before it is released as CH4), and τbios is the mean biospheric turnover time.
Historical global atmospheric Δ14C‐CO2 observations were taken from Graven et al. (2017) over 1850–2015
(yearly) and Reimer et al. (2013) before 1850. λr is set to be 8,267 years. R14C_bios was simulated for τbios of 1–
12 years with 1‐year increments over 1750–2015, and then interpolated for fractional year values of τbios.
2.2. Particle Filter Approach
We used the particle filter (PF) approach based on a Monte Carlo (MC) method for non‐Gaussian nonlinear
filtering and smoothing (Doucet et al., 2001; Kitagawa, 1996) to estimate the posterior distributions of 20 pa-
rameters in CH4 sources and sinks—the scaling factors, which adjust the prior CH4 emissions and loss rates ( f ),
δ13C and δD source signatures, KIEC, KIED, τbios, and ϕ (Table 1 and Equations 1–6)—over 1750–2015. In the
PF, conditional probability density functions are approximated by successive prediction and filtering of many
realizations of the state variables (hereafter called “ensembles”). Each ensemble is propagated in time according
to the model equations (Equations 1–4) with the 20 parameters (i.e., prediction). The ensemble is compared to
observations and either accepted or rejected using the likelihood function of the observations (i.e., filtering). The
prediction and filtering stage is repeated until the final observation target year, 2015, and finally a time series of
posterior parameter distributions that match all the observation targets from 1750 to 2015 is extracted (i.e.,
smoothing). For the base simulation, we adopted 100,000 realizations for each emission scenario, which were
separated into 50 sets of 2,000 ensembles to utilize a parallel computational technique.
The details of the PF procedure are described as follows. First, initial ensembles of the 20 parameters were
randomly generated from their full initial ranges using Latin hypercube sampling. The first target year, 1750, was
then compared to a 50‐year spin‐up simulation where all parameters were prescribed to be constant at the initial
values (see Text S1 in Supporting Information S1 for more details). From 1750, each ensemble of the 20 pa-
rameters, θ, is assumed to follow a random walk model θ t = θ t−1 + ut, where t represents a time step consisting of
51 target years over 1750–2015 (Table S1 in Supporting Information S1), and ut is assumed to follow Gaussian
distributions. Potential time variation in parameters after 1750 is thus included by resampling the accepted pa-
rameters with adding Gaussian noise ut whose standard deviation is α% of the initial parameter ranges, where α is
also estimated by the PF for each parameter of each target year. The prior distribution of α is assumed to be
uniform whose upper and lower bounds are set to be [0, 10], except time‐invariant parameters (geological source
parameters, Egeo, δ13Cgeo, and δDgeo), whose α is fixed at 0.3. A sensitivity test was performed to investigate the
impact of setting all isotopic parameters to be time‐invariant (IsoParaFixT; Table S3 in Supporting Information
S1). The parameter values for the period between the adjacent target years are linearly interpolated. When the
predicted θt exceeds the upper or the lower bound of the initial prior parameter ranges (Table 1), the θt is replaced
by θt−1 to avoid divergence from prior knowledge.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
4 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 5 ---
For each prediction stage, the number of ensembles was amplified by 10; that is, 2,000 × 10 ensembles were
generated at each target year for each 50 parallel computation. This is effective to avoid “particle degeneracy”—
when only a small number of ensembles has a nonzero importance weight through the filtering and thus the PF
approach fails to accurately reproduce the posterior distributions of interest (Doucet et al., 2001). The log like-
lihood of each of the 20,000 ensembles in each parallel computation was calculated, and 2,000 new ensembles
were created based on the likelihood and sequential importance sampling with replacement (Doucet et al., 2001;
Kitagawa, 1996). The likelihood of each ensemble was computed based on the prescribed observation targets
(Table S1 in Supporting Information S1). After the filtering stage in 2015, the filtered ensembles at each time step
were sequentially resampled from the stored likelihood to obtain the conditional joint distribution for all time
steps. Thus, a time series of posterior parameter distributions that match all the observation targets for 1750–2015
were extracted (see Kitagawa, 1996; Doucet et al., 2001 for more details).
2.3. Parameters in CH4 Sources and Sinks
Table 1 shows a summary of the 20 parameters in CH4 sources and sinks. Because our prior knowledge on source
and sink parameters is uncertain, we specified all parameter ranges to be quite wide in recognition of their un-
certainties and realistic boundaries. We assumed that applying a subjective prior mean and standard deviation in
prior Gaussian distributions extrapolated from current limited observational evidence (e.g., prior isotopic source
signatures during a historical period) could introduce biases in their posterior estimates. As a compromise, we
applied an initial uniform distribution with wide upper and lower bounds of each parameter, which were estimated
from the literature (Table 1), and then utilized our atmospheric observational target to progressively optimize the
parameters (see Section 3.1).
The scaling factors, which adjust the prior anthropogenic BIO, natural BIO, and anthropogenic FF CH4
emissions ( fanth_bio, fnatr_bio, and fanth_ff, respectively), were set to be 1.0 [0.5, 1.5] (mean and minimum–
Table 1
Summary of 20 Parameters and Their Ranges Used in Our Base Simulation
Parameter
Mean [min., max.]
Definition
fanth_bio
1.0 [0.5, 1.5]a, b, c
Scaling factor that adjusts the prior anthropogenic BIO CH4 emission
fnatr_bio
1.0 [0.5, 1.5]a, b, c
Scaling factor that adjusts the prior natural BIO CH4 emission
fanth_ff
1.0 [0.5, 1.5]a, b, c
Scaling factor that adjusts the prior anthropogenic FF CH4 emission
fbb
2.0 [0.5, 3.5]a, b, c
Scaling factor that adjusts the prior BB CH4 emission
Egeo
40 [0, 80]d, e
GEO CH4 emission (Tg CH4 yr−1)
τbios
6.5 [1, 12]f
Biospheric turnover time (year)
ϕ
230 [80, 380]g
NPP 14CH4 emission factor (GBq/GWa)
floss
1.0 [0.9, 1.1]h
Scaling factor that adjusts the prior total CH4 loss rate
KIEC
1.0065 [1.005, 1.008]a, b
Sink‐weighted total KIEC
KIED
1.275 [1.25, 1.30]a, b
Sink‐weighted total KIED
δ13Canth_bio
−62.2 [−65.4, −59.0]a
δ13C‐CH4 for anthropogenic BIO source (‰)
δ13Cnatr_bio
−62.2 [−65.4, −59.0]a
δ13C‐CH4 for natural BIO source (‰)
δ13Canth_ff
−44.0 [−46.8, −41.2]a
δ13C‐CH4 for anthropogenic FF source (‰)
δ13Cbb
−22.2 [−29.8, −14.6]a
δ13C‐CH4 for BB source (‰)
δ13Cgeo
−49.0 [−52.0, −46.0]i
δ13C‐CH4 for GEO source (‰)
δDanth_bio
−317 [−332, −302]j
δD‐CH4 for anthropogenic BIO source (‰)
δDnatr_bio
−317 [−332, −302]j
δD‐CH4 for natural BIO source (‰)
δDanth_ff
−197 [−212, −182]j
δD‐CH4 for anthropogenic FF source (‰)
δDbb
−211 [−226, −196]j
δD‐CH4 for BB source (‰)
δDgeo
−197 [−212, −182]j
δD‐CH4 for GEO source (‰)
aSchwietzke et al. (2016). bFujita et al. (2020). cSaunois et al. (2020). dEtiope and Schwietzke (2019). eHmiel et al. (2020).
fLassey, Etheridge, et al. (2007). gGraven and Gruber (2011). hPrather et al. (2012). iEtiope et al. (2019). jSherwood
et al. (2017).
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
5 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 6 ---
maximum range), and that for BB CH4 emissions ( fbb) to be 2.0 [0.5, 3.5]. They were approximately lower and
upper bounds of previous estimates of top‐down and bottom‐up CH4 emissions when these scaling factors were
applied to our prior emissions (Fujita et al., 2020; Saunois et al., 2020; Schwietzke et al., 2016). For geologic
CH4 emissions (Egeo), the range was set to be 40 [0, 80] Tg CH4 yr−1. The lower bound was taken from the
atmospheric Δ14C‐CH4‐based estimate (Hmiel et al., 2020), whereas the mean and upper bound was taken from the
current bottom‐up estimate (Etiope & Schwietzke, 2019). The range in mean biospheric turnover time (τbios) was
set to be 6.5 [1, 12], which was taken from the best estimate of Lassey, Etheridge, et al. (2007) but with larger
uncertainty. The range of NPP 14CH4 emission factor (ϕ), 230 [80, 380], was adopted from a 70% confidence
interval (CI) of the total PWR 14C emissions from Graven and Gruber (2011) after multiplying it by 72% to extract
14CH4 emissions only (Zazzeri et al., 2018). The range of ϕ covers the previous observation‐based estimates in
Kunz (1985) and Eisma et al. (1995).
The scaling factor for the total CH4 loss rate ( floss) was set to be 1.0 [0.9, 1.1], following ± 1 SD of Prather
et al. (2012). The prior mean of total KIEC and KIED were set to be the same as Fujita et al. (2020) (1.0065 and
1.275) and similar to Schwietzke et al. (2016) for KIEC (1.0063), so as to directly compare our results with the two
isotopic modeling studies. The prior sink‐weighted total KIEC and KIED ranges were set to be [1.005, 1.008] and
[1.25, 1.30], respectively, based on average sink fractions in Saunois et al. (2020) with tropospheric Cl sink of 3–
11 Tg/yr and their experimental KIEs from the literature (Table S4 in Supporting Information S1). The mean δ13C‐
CH4 and δD‐CH4 isotopic signatures for each source were taken from database‐derived estimates in Schwietzke
et al. (2016) and Sherwood et al. (2017), respectively, except δ13Cgeo taken from Etiope et al. (2019). Despite
characterizing global mean source signatures by Schwietzke et al. (2016) and Sherwood et al. (2017), it is known
that their database tends to be spatially biased—a large part of the data set was sampled in North America and only a
few data were available in the tropics, especially for nonfossil sources (see Figure 2 of Sherwood et al., 2017).
Because this spatial bias has not changed dramatically in their updated database (Sherwood et al., 2021), in which
they did not report global mean signatures, here, we refer to Schwietzke et al. (2016) and Sherwood et al. (2017) as
current database‐driven global mean signatures. We thus set the uncertainty ranges of isotopic source signatures
quite wide, ±4 SD of Schwietzke et al. (2016) for δ13C‐CH4 and ±15 permil for δD‐CH4. Mean values of each
parameter range (Table 1) were used when performing prior atmospheric simulations, as presented in Figure 1.
Sensitivity tests were performed to investigate the impact of these parameter choices (ParaRange; Table S3 in
Supporting Information S1). A wider prior KIEC range [1.005, 1.010] was applied to consider potential maximum
tropospheric Cl contributions (Table S4 in Supporting Information S1; with tropospheric Cl sink of 35 Tg/yr)
(ParaRange #5). Many sensitivity tests were also performed by applying different ranges of specific isotopic
parameters or by fixing the parameters as perfectly known parameters (ParaRange #1–4, #6–13). The impact of
prior ranges of source scaling factors was also examined (ParaRange #14 and #15).
2.4. Observation Targets
We set atmospheric CH4, δ13C‐CH4, δD‐CH4, and Δ14C‐CH4 observational target ranges for 51 target years:
1750, 1850, 1900, 1950, 1960, and every year for 1970–2015 (Figure 1, Figure S1 and Table S1 in Supporting
Information S1). The target years were chosen to cover the general features of global means and trends over 1750–
2015 with a discrete time space. Similar to parameter ranges, all observational ranges were specified to be quite
wide in recognition of the uncertainty in the observations, especially during the early historical period, consid-
ering their global representativeness. Due to the limited spatiotemporal coverage of atmospheric observations,
especially for δD‐CH4 and Δ14C‐CH4, we adopted multidecadal blocks of all observational targets before 1970.
The CH4 observation targets were taken from Meinshausen et al. (2017), a historical global CH4 data set combining
Law Dome and NEEM Greenland ice core data for 1750–1983, and from NOAA Global Monitoring Laboratory
(NOAA/GML) CH4 data for 1984–2015 (Dlugokencky et al., 2021). The observational targets for 1750–2015 were
specified as Gaussian distributions with means and 1 SD uncertainties. Uncertainties of 20 ppb for 1750–1950, of
10 ppb for 1960–1984, andof 5 ppb after 1984were prescribed, considering the uncertainties of age of air in ice core
data before 1984, in sample measurements, and in reconstruction of global annual means.
Because there is no representative historical global mean data set for δ13C‐CH4 before 1984, and δD‐CH4 and
Δ14C‐CH4 over 1750–2015, we reconstructed these using available data sets (Ferretti et al., 2005; Fujita
et al., 2020; Hmiel et al., 2020; Lassey, Etheridge, et al., 2007; Michel et al., 2021; Mischler et al., 2009; Rice
et al., 2016; Schaefer et al., 2016; White et al., 2016) (see Figure S1 and Text S1 in Supporting Information S1).
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
6 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 7 ---
Only upper and lower bounds of their global means were prescribed as
observation targets until 1978 for δ13C‐CH4 and δD‐CH4 and until 1979 for
Δ14C‐CH4 using available ice/core firn data (Ferretti et al., 2005; Hmiel
et al., 2020; Lassey, Etheridge, et al., 2007; Mischler et al., 2009). This was
due to the limited number of data, as well as limited time and space repre-
sentativeness of these observations over the period (Text S1 in Supporting
Information S1). After the 1970s, the global means and 1 SD uncertainties of
δ13C‐CH4, δD‐CH4, and Δ14C‐CH4 were specified. For 1978–1983, the
northern composite δ13C‐CH4 data set in Rice et al. (2016) was utilized to
reconstruct annual global averages. Subsequently, annual mean globally
averaged δ13C‐CH4 for 1984–2013 combining the Institute of Arctic and
Alpine Research (INSTAAR)/NOAA for 1999–2013 (Michel et al., 2021)
and the National Institute of Water and Atmospheric Research (NIWA) for
1984–1998 (Schaefer et al., 2016), compiled in Schwietzke et al. (2016), were
used. The uncertainties of the global δ13C‐CH4 averages were prescribed to be
0.1‰ since 1984, as used in Schwietzke et al. (2016). For δD‐CH4, the
northern composite δD‐CH4 data set in Rice et al. (2016) was also utilized to
reconstruct global averages for 1978–2005, followed by global averages
estimated based on global air sampling networks (Fujita et al., 2020; Rice
et al., 2016; White et al., 2016). For Δ14C‐CH4, the annual mean global av-
erages were constructed using the ice/core firn data set for Δ14C‐CH4 (Hmiel
et al., 2020). The mean and uncertainties of global δD‐CH4 and Δ14C‐CH4
averages were estimated based on MC simulations (see Text S1 in Supporting
Information S1 for more details). The mean and uncertainty of targets, for
which the values were not prescribed, were linearly interpolated using the
adjacent data.
We assumed the atmospheric burden is directly proportional to the global
mean surface mole fractions at 2.75 Tg CH4 ppb−1 (Prather et al., 2012). This
includes the ratio of the integrated burden of the observed vertical profile of
CH4 mole fractions (i.e., surface to stratosphere) relative to that if it were
uniformly mixed throughout the atmosphere, the value being 0.973 (Prather
et al., 2012). Here, we also applied the same conversions for 13CH4, CH3D,
and 14CH4, as done in previous box model studies (e.g., Lassey, Etheridge,
et al., 2007; Schwietzke et al., 2016), although stratospheric δ13C‐CH4, δD‐
CH4, and Δ14C‐CH4 differs from the surface values. However, because the
amount of CH4 in the stratosphere is much lower than in the troposphere, we
confirmed the impact of these differences are within the limits of the un-
certainties we consider and therefore do not affect our conclusion (Text S1 in
Supporting Information S1).
Sensitivity tests were performed to investigate the impact of each atmospheric isotopic observational constraint
by applying different combinations of observational constraints (Obs; Table S3 in Supporting Information S1).
The impact of potential interlaboratory differences of isotopic measurements was also examined (ObsIsoILD;
Table S3 in Supporting Information S1).
While the use of the one‐box model removes information contained in spatial gradients, we chose to follow this
approach based on the sparse data coverage and the computational efficiency of the one‐box model for exploring
many parameter uncertainties and sensitivity tests. The limitations of our one‐box model approach are discussed
further in Section 4.3.
2.5. Observational Estimates of Global Nuclear Power Plant 14CH4 Emission Factor
Based on the European RAdioactive Discharges Database (RADD, 2017) of 14C emissions and the IAEA PRIS
database of nuclear power generation (IAEA PRIS, 2017), Zazzeri et al. (2018) calculated global 14CH4 emissions
from PWRs for the period of 1972–2016 by applying the observed lognormal emission factor distributions for
Figure 1. Simulated atmospheric CH4 and isotopic histories compared to
observation‐based target ranges. Time series of simulated atmospheric CH4
(a), δ13C‐CH4 (b), δD‐CH4 (c), and Δ14C‐CH4 (d) are presented in CEDS
(red), EDGARv5 (blue), and EDGARv6 (green) prior and posterior
scenarios over 1750–2015. Posterior mean values are shown in solid lines,
and colored bands mark the 68% CI (given by 16th and 84th percentiles),
which are available in Dataset S1. Dotted lines show prior mean values.
Black bars show prescribed global observational target ranges (cap only after
1970). Observations and target ranges are also shown in Figure S1 and Table
S1 in Supporting Information S1. Note the time axis before 1950 is rescaled.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
7 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 8 ---
PWRs in 600 MC simulations to global power generation data. In this study, we updated their results by applying
several changes: (a) The data from France, reported in RADD (2017), were excluded from the analysis due to their
constant emission factors, suggesting that these values may not have been derived from empirical measurements.
(b) Separate observation‐based lognormal distributions were used for the Soviet‐design VVER reactors (Zazzeri
et al., 2018) (−0.90 and 0.29 for the log of the mean and standard deviation, respectively, in TBq/GWa) and for all
other PWR reactors (−1.65 and 0.93). (c) A fraction of 14C released as non‐CO2 from the PWRs was estimated
based on the measurements of total 14C and 14CO2 emissions from each 20 reactors reported in RADD averaged
for 1995–2015 (mean: 75%, min: 44%, and max: 95%), not fixed at 72% as in Zazzeri et al. (2018). (d) The organic
fraction of 14C released as non‐CO2 from PWRs that is 14CH4 was assumed to be a uniform distribution ranging
68%–77%, based on earlier measurements of organic 14C species in PWRs (Kunz, 1985), not 100% as in Zazzeri
et al. (2018). (e) The total MC simulation number was set to be 10,000, not 600 in Zazzeri et al. (2018). We thus
conducted new MC simulations including these changes and estimated the 14CH4 NPP emission factors (ϕ) and
their 95% CI (given by 2.5th and 97.5th percentiles).
3. Results
3.1. Global CH4 Emissions, Sinks, and Parameters
Figure 1 shows simulated atmospheric CH4, δ13C‐CH4, δD‐CH4, and Δ14C‐CH4 under our base simulation,
compared to the observation‐based target ranges. The posterior parameter ensembles reproduce observed at-
mospheric histories well, whereas the prior mean scenarios do not match observations. The prior scenarios differ
by using CEDS, EDGARv5.0, or EDGARv6.0 for anthropogenic emissions but otherwise share the same
emissions, sink, and parameters. In the prior scenarios, there are large overestimations of CH4 and un-
derestimations of δ13C‐CH4, whereas the observed trends of δD‐CH4 and Δ14C‐CH4 are generally captured but
with slight underestimations, particularly in Δ14C‐CH4. These discrepancies are resolved with plausible com-
binations of optimized parameters that reproduce all the atmospheric CH4 tracers simultaneously in the posterior
ensembles (Figure 1).
The time series of the posterior 20 parameter ensembles in CEDS, EDGARv5, and EDGARv6 scenarios are
shown in Figure 2. Histograms of these parameters averaged for the period 2003–2012 are shown in Figure 3. As
described in Section 2.3, the prior initial distributions of all these parameters (corresponding to the vertical axis
range in Figure 2 and gray lines in Figure 3) were specified to be quite wide. Despite the weak prior constraints,
the posterior distributions of fbb, fanth_bio, fnatr_bio, fanth_ff, Egeo, ϕ, τbios, floss, KIEC, KIED, δ13Canth_bio, δ13Cnatr_bio,
and δ13Canth_ff are narrowed down from the prior whereas δ13Cgeo, δ13Cbb, δDanth_bio, δDnatr_bio δDanth_ff, δDgeo,
and δDbb are not changed so much (Figure 3), indicating the different importance of each parameter for repro-
ducing atmospheric observations under our model settings. fanth_bio and fanth_ff are independently optimized
against three prior anthropogenic emission scenarios (Figures 2b and 2d), such that the scaling factors do not
correspond to the same emissions totals, whereas the other parameters are optimized from the same priors for all
scenarios.
Much lower fnatr_bio and Egeo than their prior means are consistent across the scenarios (Figures 2c and 2e). The
posterior fbb shows that posterior BB emissions up to 3 times larger than in the prior (van Marle et al., 2017) until
1980 and 2 times larger in the 2000s, which is also consistent across the three scenarios (Figure 2a). The posterior
floss shows a slight upward shift from the prior mean until the late 1980s, followed by a gradual decrease until 2015
(Figure 2h), which slightly weakens the prior increasing OH trend since 1980 (see Section 2.1). For isotopic
parameters, posterior BIO δ13C‐CH4 source signatures (δ13Canth_bio and δ13Cnatr_bio) and KIEC are higher than
their prior means (Figures 2i–2l and 3i–3l). Slightly higher δ13Canth_ff and KIED and lower τbios from their prior
means are also obtained (Figures 2g–2j, 2m, and 3g–3j and 3m). The posterior mean ϕ is consistent with its prior
mean, but with significantly narrowed distributions after late 1980 (Figures 2f and 3f).
To show how the posterior distributions change over time as atmospheric constraints filter the ensembles, the
histograms of the 20 parameters for the EDGARv6 scenario in the filtering stage of selected target years are
shown in Figure 4 (for 1750–1960) and Figure 5 (for 1970–2010). Already in 1750, Egeo, fnatr_bio, fbb, floss,
δ13Cnatr_bio, KIEC, and KIED are optimized from the prior setting based on the atmospheric target in 1750
(Figures 4a–4c 4e, 4h–4j, and 4l). After 1900, fanth_bio, fanth_ff, and δ13Canth_bio are optimized as anthropogenic
emissions become larger (Figures 4b–4d and 4k). τbios is optimized after 1960 when biospheric 14CH4 emissions
increase rapidly after nuclear bomb testing (Graven et al., 2017) (Figure 4g). The NPP emission factor, ϕ, is
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
8 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 9 ---
Figure 2. Time series of posterior 20 parameter ensembles in CEDS (red), EDGARv5 (blue), and EDGARv6 (green) scenarios for 1850–2015 under the base simulation.
Posterior mean values are shown in solid lines, and colored bands mark the 68% CI. Each vertical axis range represents the initial prior range of that parameter.
Figure 3. Histograms of posterior 20 parameter ensembles in CEDS (red), EDGARv5 (blue), and EDGARv6 (green) scenarios averaged for the period 2003–2012 under
the base simulation. Also shown are their initial uniform prior distributions (gray).
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
9 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 10 ---
optimized after the late 1980s when NPP 14CH4 emissions rise due to the installation and increased power
production of NPPs (Zazzeri et al., 2018) (Figure 5f). The 14CH4 emissions from BIO sources after the 1950s and
then from NPPs after the 1980s are reflected in the observed atmospheric trends in Δ14C‐CH4 (Figure 1d) (Lassey,
Etheridge, et al., 2007). These results show that several parameters are sensitive to the specific observations in
Figure 4. Same as Figure 3, but shown for the initial prior distributions and the distribution in the filtering stage of selected target years, 1750, 1850, 1900, 1950, and
1960. Here, results of only the EDGARv6 scenario are presented. See Figure 5 for subsequent target years.
Figure 5. Same as Figure 4, but for selected target years of 1970, 1980, 1990, 2000, and 2010.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
10 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 11 ---
different periods, and that not all 20 parameters are simultaneously optimized in each target period (i.e., not all
parameters are necessarily correlated).
Figure 6 shows the time series of the posterior global CH4 emissions and sinks in units of Tg CH4 yr−1, which
allows an easier comparison between the different scenarios and evaluation in the context of the global CH4
budget. Posterior anthropogenic FF emissions are not significantly higher than the prior emissions from the
bottom‐up inventories, except for EDGARv6 in the 1970s (Figure 6c). The posterior FF emissions from the three
scenarios are consistent with each other and significantly lower than the prior emissions in EDGARv5 in the
1970s and CEDS after 2002 (Figure 6c). The rapid growth in the 1970s in EDGARv5, driven by the Middle East
and Africa (i.e., oil producing countries), appears to be revised downward too strongly in the newer version
EDGARv6, while the growth after 2002 in CEDS driven by China (mainly coal) seems to be overestimated. Much
lower posterior natural BIO and GEO emissions than bottom‐up priors (Etiope & Schwietzke, 2019; Saunois
et al., 2020) (Figures 6e and 6f) account for the overestimation in total CH4 emissions (Figure 6a) and simulated
atmospheric CH4 (Figure 1a) in prior scenarios. Although our isotope‐based approach cannot in principle
differentiate anthropogenic from natural BIO sources and their trends over the industrial period, the overall
overestimation of BIO sources cannot be attributed to anthropogenic BIO because it was present already in 1750,
when anthropogenic BIO sources were small. Because GEO and BB CH4 emissions are relatively small, there is
no other way to match atmospheric CH4 concentrations in 1750. The posterior OH anomaly, derived from the
product of our posterior floss (Figure 2h) and prior OH anomaly taken from multimodel ESMs (Stevenson
et al., 2020), shows a slightly weaker but increasing trend following the prior over 1980–2015 (Figure 6g).
Figure 6. Prior and posterior CH4 emissions and sinks by sectors for 1850–2015. Time series of global total (a),
anthropogenic biogenic (b), anthropogenic fossil fuel (c), and biomass burning CH4 emissions (d), and tropospheric OH
anomaly (g) as well as averaged natural biogenic (e) and geologic (f) CH4 emissions. The OH anomaly is derived from the
product of our prior OH anomaly taken from Stevenson et al. (2020) (dotted line in Figure 6g) and our posterior floss. Color
and line styles in panels (a–d and g) are same as Figure 1. Markers and error bars in panels (e, f) represent mean values and
68% CI, but for the mean values and full range in prior. Details of prior emissions and parameter setting are presented in
Table S2 in Supporting Information S1 and Table 1, respectively.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
11 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 12 ---
Because the posterior results among CEDS, EDGARv5, and EDGARv6 scenarios are consistent, hereafter, we
refer to the average of the three scenarios as our posterior global CH4 budget.
We calculate decadal averages of each scenario for 2003–2012 and 1986–2000, and compare our results with
recent GCP estimates (Saunois et al., 2020) and isotopic studies (Fujita et al., 2020; Hmiel et al., 2020;
Schwietzke et al., 2016), as well as the most recent Δ14C‐CH4 study estimating global FF emissions from their
Δ14C‐CH4 data (Lassey, Lowe et al., 2007) (Table 2). Our global total CH4 emissions (∼568 Tg CH4 yr−1) are
similar to the top‐down GCP estimates, as expected because our total CH4 lifetime (∼9 years), based on Prather
et al. (2012), also resembles that in the GCP estimates. The BIO and BB emissions are also similar between
ours and top‐down GCP estimates, which are larger and smaller than those in stable isotope estimates,
respectively.
To compare our results for anthropogenic FF emissions to previous studies, Figure 7 shows our average posterior
anthropogenic FF emissions, together with previous bottom‐up and top‐down estimates. Our posterior anthro-
pogenic FF emissions for 2003–2012 (128 [103, 152] Tg CH4 yr−1; mean and 68% CI, given by 16th and 84th
percentiles) are lower than previous isotopic‐based estimates and are not consistent with their negative or zero FF
trends after 2007 (Fujita et al., 2020; Hmiel et al., 2020; Schwietzke et al., 2016). Between 2000–2006 and 2007–
2013, our posterior estimates indicate an increase in anthropogenic FF emissions (14.2 [6.3, 22.3] Tg CH4 yr−1),
an increase in total BIO emissions (16.1 [8.1, 24.1] Tg CH4 yr−1), a slight decrease of BB emissions (−5.0 [−8.4,
−1.5] Tg CH4 yr−1), and a slight increase of the total CH4 loss rate (1.5 [0.3, 2.7]%). However, the interpretation
of recent CH4 growth is complicated by poorly constrained global OH trends (see Section 3.3). A newer version of
CEDS, prepared for CMIP7 experiments (O'Rourke et al., 2021), shows that the FF emission increase after 2002
was revised downward compared to the previous CEDS emissions, while the FF emissions in 1970s were strongly
increased, which is similar to EDGARv5 but inconsistent with our results. The UNFCCC inventory for
anthropogenic FF emissions, compiled as the Global Fuel Emissions Inventory version 2 (GFEIv2; Scarpelli
et al., 2022), is much lower than the other estimates.
Table 2
Summary of Averaged Posterior Global CH4 Budget From Our Base Simulations and Previous Top‐Down Estimates
This studya
Saunois et al. (2020) b
Schwietzke
et al. (2016)
Fujita
et al. (2020)
Lassey, Lowe, and
Smith (2007)
Hmiel
et al. (2020)c
Period
1986–2000
2003–2012
2008–2017
2008–2017
2003–2013
2003–2012
1986–2000
2003–2013
Atmospheric constraints
CH4, δ13C, δD, Δ14C
CH4 (Top‐
down)
None
(bottom‐up)
CH4, δ13C
CH4,
δ13C, δD
CH4, Δ14C
CH4, δ13C,
Δ14C
Total emissions
(Tg CH4 yr−1)
536 [506, 564] 568 [532, 601]
576 ± 15
737 ± 98
593
558
560 ± 40
–
Total Biogenic emissions
(Tg CH4 yr−1)
384 [360, 409] 406 [379, 433]
427 ± 21
531 ± 44
355 ± 27
346
–
–
Biomass burning Emissions
(Tg CH4 yr−1)
37 [28, 45]
31 [21, 41]
30 ± 5
30 ± 5
43 ± 9
50
–
–
Anthropogenic fossil emissions
(Tg CH4 yr−1)
112 [93, 130]
128 [103, 152]
111 ± 17
128 ± 14
145 ± 23
162
168 ± 16
177 ± 37
Geologic emissions
(Tg CH4 yr−1)
3.4 [1.0, 6.7]
8 ± 3
45 ± 14
51 ± 20
1.6 [0, 5.4]
Total fossil fraction (%)
21 [18, 25]
23 [19, 27]
21 ± 3
24 ± 4
33 ± 5
29
30 ± 2
–
Note. Here CEDS, EDGARv5, and EDGARv6 scenario results are averaged. Uncertainties are reported as 68% CI (this study) or 1 SD, (previous studies), except for
geologic emissions in Hmiel et al. (2020) reported as 95% CI. aGeologic emissions are presented for the average of 1850–2015 since they are assumed to be
time‐invariant. bAll 1 SD values of Saunois et al. (2020), presented here, are roughly estimated from the minimum and maximum values of corresponding emission
categories in Table 3 of Saunois et al. (2020). The “other natural sources” (37 Tg CH4 yr−1) of top‐down estimates, presented in Saunois et al. (2020), is assigned to
geologic emissions by 8 Tg CH4 yr−1 (i.e., geological, permafrost soil, and hydrates) and natural biogenic emissions by 29 Tg CH4 yr−1 (i.e., freshwater, wild animals,
termites, and biogenic ocean) based on the proportion of bottom‐up estimates for the same period. cOnly preindustrial Δ14C‐CH4 and modern δ13C‐CH4 data are used.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
12 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 13 ---
3.2. Correlations in Global CH4 Budget
Next, we explore the correlations between our posterior source emissions and parameters. Because we also
optimize the total CH4 loss rate, which is strongly correlated with posterior emission strength (Figure S2 in
Supporting Information S1), we present correlations with source fractions—the proportion of global total CH4
emissions as specific source CH4 emissions (Figure 8). Here, global total BIO (anthropogenic plus natural BIO),
global total FF source (anthropogenic FF plus GEO), and BB source fractions, averaged over 2003–2012, are
presented. Similarly, we calculate total BIO and FF isotopic source signatures (δ13Cbio, δ13Cff, δDbio, and δDff) by
emission‐weighted means derived from natural and anthropogenic sources.
A high correlation (|R| ≥0.5) is observed between all source fractions and ϕ (Figures 8ab, 8ac, and 8ad), and
between total BIO fraction and δ13Cbio and KIED (Figures 8d and 8y), indicating the importance of these pa-
rameters for estimating global sectorial source fractions under our model settings. Skewed distributions are
observed in posterior KIEC around the upper bound of our prior range, which could affect the correlation between
sectorial source fractions. To extract the primary correlations in the global CH4 budget shown in Figure 8, we
focus on the relationships between BIO and FF fractions with δ13Cbio and ϕ in Figure 9 and compare our results
with those in previous studies.
For global total FF source fractions versus global total BIO source fractions averaged over 2003–2012 (Figure 9a),
a strong negative correlation (R = −0.90) is found, as expected because these are the two major source fractions
(>90%). Deviation from a straight line arises from differences in the BB fraction. Although our all posterior en-
sembles cover all estimates in previous studies presented here, we find our posterior mean FF fraction, 23.1 [19.0,
26.8] % (mean and 68% CI), is generally lower than those in stable isotope‐based studies (28%–33%) (Basu
et al., 2022; Fujita et al., 2020; Lan et al., 2021; Schwietzke et al., 2016; Thanwerdas et al., 2022) and more
Figure 7. Time series of global anthropogenic fossil CH4 emissions from 1970. Our posterior mean and 68% CI, derived from averages of CEDS, EDGARv5, and
EDGARv6 scenarios, are presented by the solid black line and the gray band, respectively. The time series data for 1970–2015 are available in Dataset S2, including other
source categories and parameters. The estimates in previous isotope‐based top‐down studies are presented by black lines: Schwietzke et al. (2016) (dotted line)a, Fujita
et al. (2020) (dash line)b, and Hmiel et al. (2020) (chain line)c. Other colored lines show different anthropogenic fossil CH4 emission inventories: CEDS version 2017‐05‐
18 (red), EDGARv5 (blue), EDGARv6 (green), EDGARv4.3.2 (Janssens‐Maenhout et al., 2019) (dashed cyan), EDGARv7 (Crippa et al., 2022) (dashed light green),
CEDS version 2021‐04‐21 (O'Rourke et al., 2021) (orange), GAINSv4—IIASA's Greenhouse gas and Air pollution INteractions and Synergies (Höglund‐Isaksson
et al., 2020) (light blue)d, IEA—International Energy Agency, Global Methane Tracker 2022 (IEA, 2022) (purple)e, and Global Fuel Emissions Inventory version 2
(GFEIv2) (Scarpelli et al., 2022)f (pink). Note that EDGARv5 is derived from EDGARv4.3.2 and that EDGARv6 derives to EDGAR7 (i.e., these lines are overlapped in
the figure, respectively). a Calculated from total fossil fuel (FF) emissions in Figure 2a of Schwietzke et al. (2016) minus geologic emissions in Table 1 of Schwietzke
et al. (2016). b Taken from total FF emissions in Figure 9a of Fujita et al. (2020) because no geologic sources are used in their prior emission. c Taken from period averages
for 2003–2012 in Hmiel et al. (2020)—total fossil emissions derived from modern atmospheric δ13C‐CH4 data in Schaefer et al. (2016) minus geologic emissions derived
from Hmiel et al. (2020)'s preindustrial atmospheric Δ14C‐CH4 data. d Taken from Figure 6b of Höglund‐Isaksson et al. (2020). e Only available in 2000, 2005, 2010, 2015,
and 2019–2021 and the emission from the bioenergy sector is excluded. f Taken from Table 1 of Scarpelli et al. (2022) and Figure 3 of Shen et al. (2023).
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
13 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 14 ---
Figure 8. Two‐dimensional histograms of our all posterior results in our base simulation (blue shades) for global total
biogenic (BIO) fraction (left column), global total fossil fuel (FF) fraction (middle column), and global biomass burning
(BB) fraction (right column) of emissions versus scaling factors of the total loss rate ( floss) and all isotopic parameters (see
Table 1) averaged over 2003–2012. Strong positive correlations (R ≥0.5) are highlighted in pink and strong negative
correlations (R ≤−0.5) in blue. Two‐dimensional histograms for other combinations of emissions and parameters are
presented in Figures S2–S4 in Supporting Information S1.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
14 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 15 ---
consistent with GCP estimates based on inversions with CH4 mole fraction only (Saunois et al., 2020) (Figures 9a
and Table 2).
Global total BIO source fraction averaged for 2003–2012 is strongly correlated with global total BIO δ13C‐CH4
source signature (Figure 9b, same as Figure 8d). Higher BIO δ13C‐CH4 source signatures correlate with higher
global total BIO fractions to balance the atmospheric 13CH4 budget, resulting in lower global total FF fraction
than in the recent isotope‐based estimates (Figure 9b and Table 2). We find our optimized total BIO δ13C‐CH4
source signature, −60.2 [−61.0, −59.7] ‰, is about 2‰ higher than those in the database‐derived estimates in
Schwietzke et al. (2016) (Figure 9b). Their database estimate of mean BIO δ13C‐CH4 source signature could
potentially be biased, because of limited data availability in the tropics where BIO isotopic signatures are higher
than those in the extratropics, and because of uncertainty in the proportions of latitudinal BIO emission strength
(Schwietzke et al., 2016; Sherwood et al., 2017). Recent studies of δ13C‐CH4 data have also used heavier total
BIO δ13C‐CH4 signatures and found higher BIO fractions than Schwietzke et al. (2016) (Basu et al., 2022; Lan
et al., 2021; Thanwerdas et al., 2022). The choice of KIEC also influences the relationship between BIO δ13C‐CH4
and total BIO source fraction, where higher KIEC is correlated with higher total BIO source fraction in the results
of Lan et al. (2021) (Figure 9b). We also found a positive correlation between total BIO source fraction and KIEC
(Figure 8m), although the strength of the correlation was not as high as for BIO δ13C‐CH4. Similar to our posterior
ensemble results, Thanwerdas et al. (2022) also present clear negative correlations between BIO δ13C‐CH4 source
signature and BIO source fraction in their sensitivity test results on the assimilation setup of δ13C‐CH4 source
signatures (Figure 9b).
There is a clear positive correlation between the total FF source fraction and the global NPP 14CH4 emissions
factor ϕ due to their opposite effects on atmospheric Δ14C‐CH4 (Figure 9c, same as Figure 8ac but for 1986–
2000). Our estimated FF fraction (21.5 [18.3, 24.7]%) and ϕ (230 [205, 256] GBq/Gwa) are both lower than
Lassey, Lowe et al., 2007 (30 ± 2.3% and 286 ± 26 GBq/GWa, mean ± 1 SD), but consistent with an earlier
estimate (Quay et al., 1999). Despite large variability in ϕ observed at individual reactors, our updated
observation‐based estimate (Section 2.5) suggests the plausible range of the global mean ϕ is only 135–213 GBq/
GWa (95% CI) for 1986–2000. This observation‐based estimate is independent from but supports our lower
posterior FF fraction (Figure 9c).
Figure 9. Two‐dimensional histograms of all posterior results (blue shades) and overall average and 68% CI (pink) for global fossil source fraction versus global biogenic
source fraction averaged over 2003–2012 (a), biogenic δ13C‐CH4 source signature versus global biogenic source fraction averaged over 2003–2012 (b), and global NPP
14CH4 emissions factor (ϕ) versus global fossil source fraction averaged over 1986–2000 (c). Black lines in (a) show the relationship under our posterior biomass
burning fractions (posterior mean and 95% CI). Black bars outside the right axis in b and c show our full prior parameter ranges. Prior mean and full ranges of our global
biogenic fraction and global fossil fractions are 72.3 [43.5–91.6] % and 23.6 [6.8–51.2] %, respectively (not shown). Gray bars in b show δ13C‐CH4 signatures (±1 SD)
from Schwietzke et al. (2016) for selected major biogenic sources, except for tropical wetlands from MOYA/ZWAMPS Team et al. (2022). Results of previous studies
are also plotted (Basu et al., 2022; Fujita et al., 2020; Lan et al., 2021; Lassey, Lowe, & Smith, 2007; Quay et al., 1999; Saunois et al., 2020; Schwietzke et al., 2016;
Thanwerdas et al., 2022) (Error bars represent 1 SD when available). The results in Quay et al. (1999) are period averages for 1990–1993, Lan et al. (2021) and Basu
et al. (2022) for 1999–2016, and Thanwerdas et al. (2022) for 2014–2015, respectively. ε in (a) and (b) represents the fractionation factor, which equals to (1/
KIEC −1) × 1,000 (‰). Gray shades in c represents our updated data‐based estimates of global NPP emission factor for 1986–2000 (95% CI) (see Section 2.5).
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
15 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 16 ---
3.3. Sensitivity Tests
To investigate the impact of different prior model settings on the estimated global source fractions, we performed
multiple sensitivity tests under (a) different observational isotope constraints (Obs; e.g., CH4 only, CH4+δ13C,
etc.) and (b) different prior ranges of selected parameters (ParaRange; i.e., changing the freedom of the pa-
rameters) (see Table S3 in Supporting Information S1). These tests are useful not only to investigate the impact of
different model settings to our base simulation results but also to directly compare our results with previous
studies by running our model with similar settings to theirs.
Figure 10 shows the correlation plots in the CH4 budget among the tests, which is the same as Figure 9 but for
overall average and 68% CI in each simulation under different observational isotopic constraints (also see Table 3
for the summary of these tests). The time series of posterior sectorial source fractions and simulated atmospheric
isotopic histories under the different isotopic constraints are presented in Figures S5 and S6 in Supporting In-
formation S1, respectively.
Comparing with CH4‐only inversion results, where the FF fraction for 2003–2012 is 23.2 [15.1, 31.6] %
(Figure 10, blue circles), incorporating δ13C‐CH4 constraints yields higher FF fractions (31.5 [27.0, 35.9] %, red
circles). This “CH4+δ13C” case is consistent with Schwietzke et al. (2016), where higher FF fractions than “CH4‐
only” inversion are obtained under additional δ13C‐CH4 constraints. This confirms that our model setup and
approach does result in higher FF fractions when only δ13C‐CH4 constraints are applied, which is similar to
previous δ13C‐CH4 based estimates (e.g., Basu et al., 2022; Lan et al., 2021; Schwietzke et al., 2016).
For a case with “CH4+Δ14C”, lower FF fractions (18.1 [13.5, 22.7] %, purple circles) are found, in comparison to
the “CH4‐only” case. This result is contrary to Lassey, Etheridge, et al. (2007), where higher FF fractions of
30 ± 2% were derived from Δ14C‐CH4 data for 1986–2000 (Figure 10c and Table 2). The difference appears to
arise from the methods used by Lassey, Etheridge, et al. (2007), who applied a regression approach rather than an
explicit model. This is discussed further in Section 4.
Figure 10. Same as Figure 9, but for overall average and 68% CI in the base simulation represented by gray shades (originally pink in Figure 9), and those in the
sensitivity tests that applied different combinations of observational constraints to the simulation (colored circles with error bars, 68% CI). Other observational or
parameter settings were kept the same as the base simulation. Results of selected previous studies (colored diamonds, mean and 1 SD) are also plotted, same as in
Figure 9. The result “Lan21” (black diamonds) is taken from their default result under ε = −7.85‰ (the same as black squares in Figures 9a and 9b). Note that clear
correlations are only seen among the scenarios in Figure 10b or Figure 10c when atmospheric δ13C‐CH4 or Δ14C‐CH4 are used as observational constraints, respectively
(i.e., In other cases, posterior mean biogenic δ13C‐CH4 signatures or NPP emission factors remain almost the same as their prior distributions).
Table 3
Summary of Our Posterior Global Total Fossil Fuel Fractions for 2003–2012 Derived From Different Observational Constraints, as Presented in Figure 10
Prior
CH4 only
CH4+δ13C
CH4+δD
CH4+Δ14C
Base (all)
Fossil fraction (%)
23.6 [17.2, 30.1]
23.2 [15.1, 31.6]
31.5 [27.0, 35.9]
23.9 [17.9, 29.8]
18.1 [13.5, 22.7]
23.1 [19.0, 26.8]
Error reduction ratio
–
−28%
31%
8%
29%
40%
Note. Uncertainties are reported as 68% CI. The error reduction ratio is defined as ‒(σpos−σpri)/σpri × 100%, where σpos and σpri are posterior and prior uncertainties,
respectively. Result under a different prior scenario excluding freshwater emissions (NoFRESHem) is also presented in Table S5 of the Supporting Information S1.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
16 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 17 ---
The mean FF fraction with the inclusion of δD‐CH4 (23.9 [17.9, 29.8] %, yellow circles) is barely changed from
the “CH4‐only” case, although the uncertainty is reduced. Such limited contributions of δD‐CH4 to the mean
sectorial fraction attribution is also seen in Fujita et al. (2020), who utilized both δ13C‐CH4 and δD‐CH4 data and
found sectorial source fractions similar to Schwietzke et al. (2016) (Figure 10a and Table 2). The potential
explanation of weak constraints by δD‐CH4 is addressed in Section 4.
With all isotopic constraints, our base simulation eventually yields a similar posterior mean FF fraction to the prior
estimate and “CH4‐only” results, but the uncertainty range is significantly reduced by 40% and 53% relative to their
estimates, respectively, as 23.1 [19.0, 26.8] % (Figure 10, gray shades) (also see Table 3). It should be noted that the
similarity between our posterior FF fraction under all isotopic constraints and those in top‐down CH4 inversions
(e.g., Saunois et al., 2020) is not an accident of our model setup, but rather the result of simultaneous constraints by
atmospheric δ13C‐CH4 and Δ14C‐CH4 (Figure 10 “CH4 + δ13C + Δ14C”, light blue). Note that the uncertainty
range in our CH4‐only results is larger by 28% than that in the prior estimate due to the inconsistent posterior
solutions among the CEDS, EDGARv5, and v6 scenarios (Figure S7 in Supporting Information S1).
Figure 11 shows the sensitivity test results that applied different prior settings of BIO δ13C‐CH4 source signatures,
KIEC and KIED (ParaRange #1–6; Table S3 in Supporting Information S1). Fixing the prior BIO δ13C‐CH4 source
signature as its prior mean (−62.2‰) yields higher FF fractions (26.6 [23.2, 29.8]) (Figure 11, blue circle), as
does fixing KIEC at its prior mean (1.0065) (24.8 [21.1, 28.6], red circle). Further increases in FF fraction are
obtained when both parameters are fixed (29.1 [26.1, 32.0], yellow circle) and even more under “CH4+δ13C”
(34.1 [30.8, 37.5], green circle), resembling the model settings and results in Schwietzke et al. (2016). Expanding
the prior KIEC range to [1.005, 1.010], considering potential maximum tropospheric Cl contributions (Table S4 in
Supporting Information S1), yields lower FF fractions, 21.1 [17.1, 25.2] (light blue circle), though within the
uncertainty of those from our base result. The posterior mean KIEC obtained from this test (1.0091 [1.0084,
1.0097]) surpasses our posterior base result (1.0075 [1.0070, 1.0078]), indicating the upper limit we used on KIEC
constrained the posterior result. Fixing the prior mean KIED (1.275) does not lead to a significant change in the
posterior mean in FF fraction but reduces the uncertainty from the base result (brown circle).
Figure 12 shows the results that applied different prior ϕ settings (ParaRange #8–13; or Table S3 in Supporting
Information S1). We find our posterior results, both in base simulation or “CH4+Δ14C”, do not change even when
our prior ϕ is replaced by Lassey et al.’s mean estimate (286 [136, 436] GBq/GWa; the min.–max. range is the
same as our base setting) or even replaced by much wider prior range (300 [0, 600] GBq/GWa) (Figure 12, blue,
red, and green circles). This indicates our posterior ϕ is well constrained by atmospheric Δ14C‐CH4 data. When
the prior ϕ is fixed at 286 GBq/GWa, however, higher mean FF fractions (∼27%) are obtained for 1986–2000 as
seen in Lassey, Lowe, et al. (2007), both in base simulation or “CH4+Δ14C” (yellow and light blue circles). We
also find the sensitivity is not significant when fixing the prior mean τbios (brown circle).
The sensitivity of the prior BB emissions are also investigated by allocating “RCO” emissions (Section 2.1) from
prior FF to prior BB emissions, in addition to the BB4CMIP (RCOem; Table S3 in Supporting Information S1),
Figure 11. Same as Figure 10, but for sensitivity tests that applied different prior mean biogenic δ13C‐CH4 source signatures, KIEC, and KIED. “CH4+δ13C” is the same
as in Figure 10.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
17 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 18 ---
showing slight lower posterior FF fractions, 21.0 [16.7, 25.2] % (and higher BB fractions), though within the
uncertainty of our base result (Figure S8 in Supporting Information S1). In this regard, our sensitivity test under a
narrower prior fbb range ([0.5, 1.5]) (ParaRange #14; Table S3 in Supporting Information S1) shows slightly
higher FF fractions of 25.3 [22.3, 28.4] % for 2003–2012 than our base simulation to compensate the posterior
lower BB fractions, despite also within the uncertainty of our base result (Figure S8 in Supporting Informa-
tion S1). Applying the default fbb range ([0.5, 3.5]) to other source scaling factors, fanth_bio, fnatr_bio, and fanth_ff
(ParaRange #15), also does not change the mean posterior results (Figure S8 in Supporting Information S1).
To investigate the impact of different prior OH and wetland emission trends, four alternative prior OH scenarios
and three alternative prior wetland scenarios are considered (OHtrend and IAWetBIOem; Table S3 in Supporting
Information S1). The results indicate different OH and wetland trend scenarios do not change the mean FF
fractions for 2003–2012 (Figure S9 in Supporting Information S1), but the different OH trends change the
attribution of the cause of the recent CH4 trend (Figure S10 in Supporting Information S1) and different wetland
emission trends change the attribution of anthropogenic and natural BIO emissions (Text S1 in Supporting In-
formation S1). Excluding prior freshwater emissions (NoFRESHem; Table S3 in Supporting Information S1) also
does not change the mean FF fractions under all isotopic constraints (“Base”) and “CH4+Δ14C” case, but
significantly changes the posterior results without constraints of Δ14C‐CH4 (e.g., “CH4 only”; see Text S1, Figure
S11, and Table S5 in Supporting Information S1), highlighting the merit of multi‐isotopic constraints including
Δ14C‐CH4 to robustly estimate the global CH4 budget.
Applying upper bounds of potential Δ14C‐CH4, δ13C‐CH4 and δD‐CH4 interlaboratory differences (ObsIsoILD;
Table S3 in Supporting Information S1) does not significantly change mean FF fractions, although the impact of
δD‐CH4 interlaboratory differences could be the most influential (Figure S12 and Text S1 in Supporting Infor-
mation S1). More careful consideration is also required if assimilating historical raw δ13C‐CH4 and δD‐CH4 data
directly, whose uncertainty of interlaboratory differences is more significant than those in modern air samples
(Umezawa et al., 2018).
4. Discussion
Several previous studies have utilized atmospheric δ13C‐CH4 as constraints for source partitioning (Basu
et al., 2022; Hein et al., 1997; Lan et al., 2021; Schaefer et al., 2016; Schwietzke et al., 2016; Thanwerdas
et al., 2022), and a few studies have further used δD‐CH4 (Fujita et al., 2020; Rice et al., 2016) or Δ14C‐CH4
(Hmiel et al., 2020; Lassey, Etheridge, et al., 2007; Quay et al., 1999), but no study synthesized all these con-
straints. This study is the first to utilize modern Δ14C‐CH4 data with available δ13C‐CH4 and δD‐CH4 data sets to
estimate the global CH4 budget and isotopic source signatures, KIEs, τbios, and ϕ over the industrial period.
Our posterior global CH4 budget is fairly consistent with atmospheric CH4‐only top‐down estimates from the
GCP (Saunois et al., 2020), but not with recent stable isotope‐based estimates (Basu et al., 2022; Fujita
et al., 2020; Lan et al., 2021; Schwietzke et al., 2016) (Figure 9a and Table 2). In this study, we optimized
Figure 12. Same as Figure 10, but for sensitivity tests that applied different prior NPP emission factors (ϕ) and biospheric turnover time (τbios). “CH4+Δ14C” is the same
as in Figure 10.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
18 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 19 ---
δ13C‐CH4 and δD‐CH4 source signatures through our PF approach, considering plausible wide uncertainties of
δ13C‐CH4 and δD‐CH4 source signatures from the database (Schwietzke et al., 2016; Sherwood et al., 2017)
(Table 1). We found that our optimized total mean BIO δ13C‐CH4 source signature (−60.2 [−61.0, −59.7] ‰) is
about 2‰ heavier than those in the prior database‐driven estimate (Schwietzke et al., 2016), whereas our total
mean FF δ13C‐CH4 source signature (−43.1 [−44.3, −41.9] ‰) is not significantly changed from the database
estimate. Recent findings show much larger tropical wetland emissions from African and Amazonian regions
(France et al., 2022; Pandey et al., 2021; Shaw et al., 2022) than previous estimates, whose δ13C‐CH4 source
signatures are heavier than at higher latitudes, −60 to −55 ‰ (e.g., MOYA/ZWAMPS Team et al., 2022).
Heavier tropical ruminant δ13C‐CH4 source signatures (−60 to −50‰) have also recently been reported (Lu
et al., 2021; MOYA/ZWAMPS Team et al., 2022). In this regard, Lan et al., 2021 presented heavier BIO δ13C‐
CH4 signatures than Schwietzke et al. (2016), utilizing the wetland δ13C‐CH4 signature map from Ganesan
et al. (2018), which considers spatial δ13C‐CH4 differences. To validate such modeled isotopic signatures maps
and the heavier global average BIO δ13C‐CH4 signatures, more direct observations are required especially in the
tropics.
Sink fractions approximately derived from our posterior total KIEC and KIED are generally consistent with
multiple‐process model estimates (Saunois et al., 2020), indicating a tropospheric Cl contribution of ∼3%
(∼18 Tg/yr under the total loss of 556 Tg/yr for 2003–2012) (Text S1 in Supporting Information S1). Our findings
suggest the minimum tropospheric Cl scenario (∼1 Tg/yr) suggested by Gromov et al. (2018) is unlikely.
Actually, when using a wider prior KIEC range [1.005, 1.010] (ParaRange #5), we obtained even higher posterior
total KIEC (1.0091 [1.0084, 1.0097] vs. 1.0075 [1.0070, 1.0078]) and KIED (1.287 [1.279, 1.295] vs. 1.283
[1.274, 1.292]). While this suggests even higher tropospheric Cl contribution (van Herpen et al., 2023), the total
KIEC also aligns with a scenario presented in Lan et al. (2021) (ε = −9.03‰, open circles in Figures 9a and 9b),
where the Cl contribution is 13 Tg/yr and the KIEC of OH (KIEC
OH) is higher, 1.0054 (Cantrell et al., 1990).
Overall, top‐down approaches can be affected by errors in KIEC and δ13C‐CH4, so improved constraints on KIEC
as well as δ13C‐CH4 signatures would help to constrain the CH4 budget. Recent studies disagree over whether
current uncertainties in KIEC or δ13C‐CH4 signatures are more important (Basu et al., 2022; Thanwerdas
et al., 2022). While our study is limited to a one‐box model with global mean values, we believe that the large
range of values we were able to consider may give a more comprehensive picture of the effect of these un-
certainties than 3D model studies that are limited to a small number of sensitivity tests (see Text S1 in Supporting
Information S1 for more details).
Our posterior FF fraction and ϕ, averaged for 1986–2000 (21.5 [18.3, 24.7]% and 230 [205, 256] GBq/GWa), are
lower than those in Lassey, Lowe, et al. (2007) (30 ± 2.3% and 286 ± 26 GBq/GWa), despite our observational
target encompassing their Δ14C‐CH4 data (Figure S1 in Supporting Information S1). To check consistency with
Lassey, Lowe, et al. (2007)'s method (“L07 method”), which used a linear regression approach to solve the mass
balance equations of atmospheric Δ14C‐CH4 and simultaneously derive total FF fraction and ϕ, we applied the
L07 method to our Δ14C‐CH4 data set over every possible 10‐year or 15‐year window over 1970–2008, assuming
that our posterior FF fraction and ϕ were the only unknowns. We found the FF fractions estimated by the L07
method vary strongly depending on the analysis period, 15.5%–34.2% for FF fraction and 159–301 GBq/GWa for
ϕ (Figure S13 in Supporting Information S1). Such large variations in FF fraction are not realistic and not
consistent with our independent observation‐based estimate of ϕ, implying that (a) there are numerous combi-
nations of FF fraction and ϕ that align with atmospheric Δ14C‐CH4 and (b) Lassey, Lowe, et al., 2007's estimate is
not necessarily the optimal one but quite sensitive to the selected data period. Our posterior ensembles encompass
Lassey, Lowe, et al., 2007's estimate, but the cumulative probability is less than 1% (see Figure 9c). Earlier Δ14C‐
CH4 studies (Manning et al., 1990; Quay et al., 1999; Wahlen et al., 1989), based on a basic box model analysis,
estimated lower FF fractions of 16%–24% (Figure 9c), which are consistent with our results. Our lower FF
fractions are also supported by our updated independent estimate from observed 14CH4 emissions (Figure 9c).
Further validation of NPP 14CH4 emissions would enable for more robust FF emission estimates, particularly if
utilizing a 3D model that requires spatiotemporally accurate prior emission data for each reactor.
Our posterior GEO emissions average 3.4 Tg CH4 yr−1, and are less than 8.8 Tg CH4 yr−1 (97.5th percentile),
which are much smaller than bottom‐up estimates (Etiope & Schwietzke, 2019; Saunois et al., 2020; Schwietzke
et al., 2016), but quite consistent with Hmiel et al. (2020). This is not surprising because we use the same ice core
Δ14C‐CH4 data with Hmiel et al. (2020) for the preindustrial era (but with a wider target range; see Table S1 in
Supporting Information S1). In contrast, our modern posterior FF emissions are smaller than in Hmiel
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
19 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 20 ---
et al. (2020), who used δ13C‐CH4 observations for 1988–2013 in Schaefer et al. (2016), not their own Δ14C‐CH4
data. Whereas Hmiel et al. (2020) reallocated CH4 emissions from GEO to anthropogenic FF sources to close the
budget, our analysis reallocates CH4 emissions from GEO to total BIO sources (Figure 9a and Table 2).
Importantly, our posterior emission scenario matches atmospheric δ13C‐CH4 and δD‐CH4 histories, suggesting
that smaller GEO and anthropogenic FF emissions are consistent with all isotopic data. In this regard, anthro-
pogenic FF emission estimates of ∼130 Tg/yr reported by Lan et al. (2021) and Basu et al. (2022), consistent to
ours, are strongly based on the prescribed GEO emissions of ∼37 Tg/yr, taken from Etiope et al. (2019). Thus,
their anthropogenic FF emissions must increase to 150–170 Tg/yr, if GEO emissions are reduced.
Our finding that average anthropogenic FF emissions for 2003–2012 are similar to bottom‐up estimates may
appear to conflict with recent studies showing underestimated fugitive CH4 emissions from oil and gas production
regions (Alvarez et al., 2018), flaring sites (Plant et al., 2022), some urban regions (Sargent et al., 2021), and some
unexpected CH4 “superemitters” (Lauvaux et al., 2022). To reconcile these findings, it could be that under-
estimated fugitive emissions are not globally significant (given our uncertainty of 24 Tg CH4 yr−1, defined as the
difference between the 84th percentile and mean), as suggested by a recent high‐resolution inversion study (Shen
et al., 2023), or that some other FF sources are overestimated in bottom‐up inventories. Several atmospheric CH4
inverse modeling studies (Saunois et al., 2020) have suggested that coal CH4 emissions in China are over-
estimated in EDGARv4.2 and even in EDGARv4.3.2 despite the revision of coal emission factors (Maasakkers
et al., 2019). Note that the fugitive CH4 emission estimates in CEDS are based on EDGARv4.2 (Hoesly
et al., 2018), that EDGARv5.0 is based on EDGARv4.3.2 (Crippa et al., 2020) (also see Figure 7), and that coal
CH4 emissions in China in EDGARv6 are even higher than those in EDGARv5.0, so the findings apply to our
three prior emissions (Text S1 in Supporting Information S1). Such overestimation of coal emissions in China (or
other biases) may therefore compensate underestimation of other FF sources.
We find higher BB fractions are required to increase both atmospheric δ13C‐CH4 and Δ14C‐CH4 levels (Figures
S5 and S6 in Supporting Information S1), similar to Hein et al. (1997), who used the FF emission estimates based
on Δ14C‐CH4 (Manning et al., 1990; Wahlen et al., 1989) and then optimized other sources based on atmospheric
δ13C‐CH4. Our posterior BB emissions during 1750–1850 are 28 [22, 34] Tg/yr, which are 2.5 [1.9, 3.0] times as
high as the BB4CMIP product used as our prior (van Marle et al., 2017). This suggests potential underestimation
in BB4CMIP, where small fires (e.g., residential heating) may not have been detected well by satellites. Since van
Marle et al., 2017 reported their products include agricultural waste burning, we did not include the BB emissions
of CEDS and EDGAR scenarios in the prior, but we instead used a wider prior fbb range in the base simulation to
encompass the potential upper bounds of BB emissions reported in top‐down estimates. More robust estimates of
prior BB emissions would enable better constraints on BB emissions and the global CH4 and isotopic CH4
budgets.
We expected that assimilating δD‐CH4 data can strongly constrain the atmospheric sink due to larger KIED than
KIEC. However, our sensitivity tests showed that whether or not δD‐CH4 data were included, the posterior floss
was not changed significantly. This is likely because (a) our prior base scenario with the tropospheric OH
anomaly derived from ESMs (Stevenson et al., 2020) has already reproduced the values and trends in our at-
mospheric δD‐CH4 target over 1750–2015 (Figure 1c) and (b) our prior ranges of respective δD‐CH4 source
signatures (±15‰) and KIED (1.25–1.30) were widely specified so that there are many combinations of pa-
rameters that can adjust the slight mismatch between observed and simulated atmospheric δD‐CH4. It is noted that
our prior time‐invariant OH scenario (OHtrend #1) did not well reproduce the rapidly increasing atmospheric δD‐
CH4 trend after 1980, potentially supporting the increasing OH scenario for the period. To further constrain the
atmospheric sink using atmospheric δD‐CH4 data, it is important to more robustly estimate prior δD‐CH4 source
signatures and KIED, as well as to strengthen the observational constraint with more observations with inter-
laboratory differences reduced.
Our posterior FF emissions remain an upward trend after 2002, which contradicts major stable isotope‐based
findings that suggest stable FF emissions and a significant rise in BIO emissions to explain atmospheric CH4
growth and δ13C‐CH4 decline after 2007 (Figures 1 and 7) (Basu et al., 2022; Fujita et al., 2020; Lan et al., 2021;
Schwietzke et al., 2016). In contrast, Worden et al. (2017) suggested from their δ13C‐CH4 box model analysis and
satellite‐based CO measurements that a decrease of BB emissions can reconcile simultaneous increase of FF and
BIO emission after 2007, similar to our posterior results. Our sensitivity tests on different prior OH trends do not
change the mean source fractions for 2003–2012 (Figure S9 in Supporting Information S1), but do change the
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
20 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 21 ---
attribution of the cause of recent CH4 trend (Figure S10 in Supporting Information S1). It is noted, however,
because our model setups do not explicitly separate the different sink fractionations among tropospheric OH and
other sinks (e.g., soil oxidations, stratospheric destructions), the decreasing OH scenarios here just need to be
viewed as decreases of the total CH4 loss rate. Thus, our sensitivity test results under decreasing OH scenarios did
not reproduce the result presented in Lan et al. (2021), where different CH4 loss processes are explicitly
considered on their δ13C‐CH4 modeling. Different prior time‐variable BIO δ13C‐CH4 signatures and KIEC
scenarios, as reported recently (e.g., Chang et al., 2019; van Herpen et al., 2023), could also impact the posterior
trends. Further studies are needed to estimate robust prior trends in OH, isotopic source signatures, and KIEs, as
well as to explicitly separate the OH and other sink fractionations in the optimization framework.
We think our simple one‐box model approach using a PF has advantages compared to previous isotopic inversion
studies by the (a) use of more isotopic tracers (δD‐CH4 and Δ14C‐CH4), (b) use of not only modern but also ice
core and firn isotopic data, and (c) more comprehensive consideration of uncertainties in isotopic parameters (i.e.,
source signatures, KIEs, ϕ, and τbios), and (d) comprehensive sensitivity tests for each observational isotopic
constraints and prior settings. This approach allowed us to optimize 20 parameters with large ensembles of
simulations and to perform many sensitivity tests. However, we acknowledge there are limitations related to our
simplized box model approach.
First, our one‐box model cannot consider the spatial information on atmospheric tracers, prior sources and sinks,
and atmospheric transport. It is well known there exists an interhemispheric difference and vertical gradient (e.g.,
troposphere to stratosphere) in atmospheric CH4 and isotopes because of the heterogeneous CH4 source and sink
distributions and atmospheric transport. The neglect of such information can weaken actual observational con-
straints and limit our analysis and discussion (Naus et al., 2019). In this regard, our purpose of this study is to
derive decadal‐scale global mean CH4 budget by synthesizing all available isotopic data since the preindustrial
era, particularly using recently published ice core and firn Δ14C‐CH4 data from 1755 to 2013 (Hmiel et al., 2020),
whose spatiotemporal density is very sparse. For a 3D model, assimilating the multiple tracers for mutidecadal
time scale is still challenging due to the computation cost, complexity of model setup, and potential overfitting to
limited data. We thus judged a simple global one‐box model is the most reasonable and practical tool for the
purpose of this study. Another challenge of our box model approach is estimating the global mean and uncertainty
of isotopic observations under such sparse data coverage. In this study, we often utilized the Arctic and Antarctic
data as the boundary values of the global mean, which could have overestimated the uncertainty. More atmo-
spheric isotopic data, especially Δ14C‐CH4, will contribute to characterizing global means more robustly and
refine the constraints provided.
Second, our posterior results still have large uncertainties on the estimated emission strengths and source and sink
parameters, especially in their trends. This is primarily due to the high degree of freedom in our box model
analysis and conservative choices for parameter ranges and observational target ranges (e.g., weak constraints on
floss by atmospheric δD‐CH4, potentially due to the high degree of freedom in δD‐CH4 source signatures and
KIED). Nonetheless, our historical atmospheric targets (even with decadal time‐window) succeeded in narrowing
down the initial parameter ranges before 1970, particularly for natural sources (i.e., Egeo, fnatr_bio, and their
isotopic source signatures), as well as after 1970 for decadal mean global CH4 budgets.
Finally, we acknowledge that multi‐isotopic inversions using 3D transport models are promising when the iso-
topic data are globally available. In this regard, δ13C‐CH4 inverse modeling is recently being attempted (Basu
et al., 2022; Thanwerdas et al., 2022), where uncertainty in tropospheric Cl contributions and KIEC of OH, as well
as BIO δ13C‐CH4 source signatures are important. It is still challenging to perform δD‐CH4 inverse modeling due
to spatially sparse atmospheric data and large uncertainties in δD‐CH4 source signatures and KIED, but further
detailed analysis of spatiotemporal variability in atmospheric δD‐CH4, in addition to δ13C‐CH4, could provide an
important constraint on CH4 sources and sinks (e.g., Warwick et al., 2016). Additional observational constraints
of CH3CCl3 or other OH tracers (e.g., Rigby et al., 2017) would also be promising to constrain OH strengths and
trends, although this also requires additional tracer parameters to be implemented and potentially optimized. For
Δ14C‐CH4, new development of CH4 sampling techniques has the potential to increase the number of Δ14C‐CH4
data (Zazzeri et al., 2021, 2023). Baseline clean data, urban polluted data, and downwind data from PWR nuclear
facilities are all valuable to better constrain CH4 sources and NPP emissions.
Journal of Geophysical Research: Atmospheres
10.1029/2024JD041266
FUJITA ET AL.
21 of 25
 21698996, 2025, 5, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD041266, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
