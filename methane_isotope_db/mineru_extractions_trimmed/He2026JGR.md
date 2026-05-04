
--- Page 1 ---
Interpreting Changes in Global Methane Budget in a
Chemistry‐Climate Model Constrained With Methane and
Isotopic Observations
Jian He1,2
, Vaishali Naik3
, and Larry W. Horowitz3
1Cooperative Institute for Research in Environmental Sciences, University of Colorado, Boulder, CO, USA, 2NOAA
Chemical Sciences Laboratory, Boulder, CO, USA, 3NOAA Geophysical Fluid Dynamics Laboratory, Princeton, NJ, USA
Abstract The continuous increase in atmospheric methane (CH4) concentrations over the past few decades
has become a major concern due to its strong role as a greenhouse gas contributing to climate change. In this
work, we investigate the changes in the global methane budget using a global chemistry‐climate model
constrained with methane and its isotopic observations. We apply spatially‐resolved isotopic signatures to better
constrain the methane sources and include methane‐hydroxyl radical (OH) feedback to better represent methane
sinks and lifetime in the model. While anthropogenic activities are found to be mainly responsible for the
methane increase since the 1980s, the increasing OH trend simulated by the model plays a critical role in the
global methane evolution. We find the observed post‐2006 shift of δ13CH4 can be explained by increases in 13C‐
depleted agricultural and waste emissions in the tropics, coupled with decreasing 13C‐enriched biomass burning
emissions and an increasing OH trend. We also find post‐2006 emission increases in energy and agriculture
sectors are large enough to offset the increasing sinks (due to increasing OH), and therefore are shown to
contribute to the post‐2006 renewed methane growth. With CH4‐OH feedback included in the model, the results
show an increasing sensitivity to emission increases on methane concentrations and lifetime. Our study
underscores the importance of OH in the global methane evolution. Neglecting changes in OH could potentially
lead to misinterpreting emission changes with respect to the long‐term observations of methane and δ13CH4.
Plain Language Summary The rapid increase in atmospheric methane concentrations in the past
several decades have drawn worldwide attention as methane is a strong greenhouse gas that contributes to
changing climate as well as a precursor to tropospheric ozone, an air pollutant. In this work, we use a three‐
dimensional computer model to comprehensively represent global atmospheric chemistry and use observations
of methane and its stable carbon isotopes to reconstruct atmospheric methane in the model to investigate the
changes in the methane emissions and methane losses. We find the increases in the methane emissions from
human activities are the major contributors to the methane increase since the 1980s. The model shows an
increasing trend in hydroxyl radical levels, the primary sink for methane and its isotopes, since the 1980s,
suggesting methane could be removed from the atmosphere more quickly. Renewed growth in methane after
2006 can be explained by the emission increases from fossil fuel extraction, and agricultural practice. Lastly,
more and continued observations are required to better understand the changes in the methane emissions and
sinks.
1. Introduction
Methane (CH4) is a powerful greenhouse gas with a global warming potential nearly 80 times higher than carbon
dioxide over a 20‐year period (Forster et al., 2021). Since the preindustrial era, atmospheric methane concen-
trations have increased dramatically, primarily due to anthropogenic activities, such as agriculture practice, fossil
fuel extraction, and waste management (Dlugokencky et al., 2011). Meanwhile, methane is removed from the
atmosphere mainly through the oxidation of the hydroxyl radical (OH), which accounts for more than 90% of total
methane sinks in addition to the smaller sinks from other chemical losses and soil uptake (Saunois et al., 2020,
2025). Given methane's relatively shorter atmospheric lifetime compared to other greenhouse gases, reducing it
can rapidly decrease global radiative forcing (UNEP, 2022). Therefore, understanding methane sources and sinks
is critical for addressing our changing climate.
Observations of atmospheric methane concentrations, such as surface monitoring data, aircraft measurements,
and satellite retrievals have been widely used to quantify the spatial and temporal distribution of methane
RESEARCH ARTICLE
10.1029/2025AV001822
Peer Review The peer review history for
this article is available as a PDF in the
Supporting Information.
Key Points:
•
Post‐2006 renewed methane growth
could be explained by the emission
increases from energy and agriculture
sectors
•
Higher tropical agricultural and waste
emissions with lower biomass burning
emissions contribute to the post‐2006
shift of δ13CH4
•
Hydroxyl radical trend plays a critical
role in driving the post‐2006 shift of
δ13CH4 and methane evolution
Supporting Information:
Supporting Information may be found in
the online version of this article.
Correspondence to:
J. He,
jian.he@noaa.gov
Citation:
He, J., Naik, V., & Horowitz, L. W. (2026).
Interpreting changes in global methane
budget in a chemistry‐climate model
constrained with methane and isotopic
observations. AGU Advances, 7,
e2025AV001822. https://doi.org/10.1029/
2025AV001822
Received 2 MAY 2025
Accepted 28 OCT 2025
Author Contributions:
Conceptualization: Jian He,
Vaishali Naik
Data curation: Jian He
Formal analysis: Jian He
Investigation: Jian He
Methodology: Jian He
Software: Jian He
Supervision: Vaishali Naik, Larry
W. Horowitz
Validation: Jian He
Visualization: Jian He
Writing – original draft: Jian He
Writing – review & editing:
Vaishali Naik, Larry W. Horowitz
© 2026. The Author(s).
This is an open access article under the
terms of the Creative Commons
Attribution License, which permits use,
distribution and reproduction in any
medium, provided the original work is
properly cited.
HE ET AL.
1 of 19


--- Page 2 ---
emissions (He et al., 2020; Jacob et al., 2022; Shen et al., 2023; Yu et al., 2021). Methane isotopic composition
(e.g., 13CH4) provides an additional constraint on specific sources due to their relatively distinct isotopic ratios
(e.g., δ13CH4), which depends on the different formation processes before methane is released to the atmosphere
(Whiticar, 1999). This allows for understanding the complex interplay of natural and anthropogenic processes
contributing to global methane levels. There are three major types of methane sources (Saunois et al., 2020): (a)
biogenic sources, where methane is produced through microbial activities (methanogenesis), such as wetlands,
rice cultivation, landfills, enteric fermentation in ruminants, show typically a lighter carbon isotopic signature
(13C‐depleted) with δ13CH4 mostly in the range of −70‰ to −50‰ (Chang et al., 2019; Sherwood et al., 2017;
Whiticar & Schaefer, 2007); (b) thermogenic sources, where methane is generated from the thermal decompo-
sition of organic matter, primarily in fossil fuel extraction, show a heavier isotopic signature with δ13CH4 mostly
in the range of −37 to −45 ‰ (Sherwood et al., 2017; Whiticar & Schaefer, 2007); (c) pyrogenic sources, where
methane is emitted from biomass burning, show a much heavier isotopic signature (13C‐enriched) with δ13CH4
mostly in the range of −17 to −26 ‰ (Dlugokencky et al., 2011).
The observed renewed methane growth since 2007 (Lan et al., 2024) and the simultaneous shift of δ13CH4
(Michel et al., 2023) toward more negative values (more 13C‐depleted) indicate that increases in biogenic sources
are the dominant drivers for the methane increase since 2007 relative to the stable period from 1999 to 2006. For
example, Schaefer et al. (2016) attributed the post‐2006 methane increase to agricultural sources based on a box
model reconstruction of CH4 and δ13CH4 time series. Similarly, with new estimates of C3‐C4 diet composition of
domestic ruminants and the evolution of δ13CH4 of enteric emissions, Chang et al. (2019) showed a significant
contribution of enteric emission increase to the total methane emission increase between 2008 and 2012, which
partly explained the observed decrease in δ13CH4. With improved wetland isotopic composition, Oh et al. (2022)
suggested the methane increase since 2007 is due to the increasing microbial emissions, more likely from wet-
lands. On the other hand, constrained by the isotopic observations post‐2006, Worden et al. (2017) found a shift of
global methane source increase from biogenic to fossil fuel emissions post‐2006 due to the influence of declining
13C‐enriched biomass burning emissions in the CH4 isotope budget, while Nisbet et al. (2016) suggested that
biogenic methane sources and not fossil fuel emissions are the dominant driver of methane increase post‐2006.
Interestingly, Chandra et al. (2024) showed total fossil fuel emissions remain stable from 2000 to 2020, but the
emissions from agriculture, landfills, as well as coal mining contributed to the post‐2006 methane increase.
Meanwhile, Skeie et al. (2023) suggested that increasing OH radicals due to anthropogenic impacts may have
contributed to the δ13CH4 shift after 2007.
A major limitation of isotopic analysis is the lack of sufficient long‐term observations to robustly represent
temporal and spatial variability for budget constraints (Lan, Nisbet, et al., 2021). Sherwood et al. (2017) high-
lighted the overlap in the isotopic source signatures by compiling data from previous studies. For example, many
studies use a global mean isotopic value (typically between −37‰ and −44‰) for fossil fuel sources (Schaefer
et al., 2016; Schwietzke et al., 2016). However, numerous measurements indicate that the δ13CH4 of fossil fuel
can be lower than −60‰, especially for oils or gases of biogenic origin (Lu et al., 2021; Menoud et al., 2022).
Using a single global mean isotopic value to constrain the global methane budget (Ghosh et al., 2015; Schaefer
et al., 2016) may lead to uncertainties when interpreting results. Therefore, it is important to consider the spatial
variability of methane isotopic source signatures.
Here, we explore the contributions of methane sources and sinks to its observed trends and variability during
1980–2017 in a global chemistry‐climate model constrained by observations. This work expands our previous
work (He et al. (2020), referred to as He2020 hereafter) by leveraging the methane isotopic observations in
addition to the methane concentration observations to constrain methane emissions. Unlike many previous studies
that either prescribe methane sinks or OH levels, we explicitly simulate sinks of methane and its carbon isotope
tracer (13CH4) in the model to better represent their atmospheric lifetime. Total methane emissions are optimized
in the model to capture the observed methane trends. We then optimize methane emissions from specific source
sectors to force the model to capture the observed δ13CH4 trends. We conduct several sensitivity simulations to
understand the uncertainties in the emission estimates associated with the energy sector, isotopic fractionation, as
well as meteorology, and explore possible drivers for methane growth in the past decades. Finally, the CH4‐OH
feedback is discussed to understand methane concentration responses to the emission changes.
AGU Advances
10.1029/2025AV001822
HE ET AL.
2 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 3 ---
2. Materials and Methods
2.1. Model Description
We use the global chemistry‐climate model developed by the Geophysical Fluid Dynamics Laboratory (GFDL) of
the National Oceanic and Atmospheric Administration (NOAA), GFDL‐AM4.1 (Horowitz et al., 2020), to un-
derstand changes in the global methane sources and sinks. A detailed description of the physics and dynamics in
AM4.1 is provided by Dunne et al. (2020) and Horowitz et al. (2020).
We follow the modeling approach in He2020. We include a representation of CH4 and 13CH4 cycles in the model
to fully characterize the drivers of methane trends and variability. Specifically, we drive the model with methane
emissions from various anthropogenic and natural sources as described by He2020 and also shown in Table S1 in
Supporting Information S1. These emissions are compiled from various inventories, including anthropogenic
methane sources from the Community Emissions Data System (CEDS) version 18 May 2017 (Hoesly et al., 2018)
for 1980–2014 and a middle‐of‐the‐road scenario of Shared Socioeconomic Pathways targeting a forcing level of
4.5 W m−2 (SSP2‐4.5) for 2015–2017 (Gidden et al., 2019), biomass burning (BMB) emissions from the
BB4CMIP database (van Marle et al., 2017) for 1980–2014 and the SSP2‐4.5 for 2015–2017, wetland (WET)
emissions from the WetCHARTs version 1.0 inventory (Bloom et al., 2017), ocean (OCN) emissions from
Brasseur et al. (1998) with near‐shore methane fluxes from Lambert and Schmidt (1993), termites (TMI) from
Fung et al. (1991), and mud volcanoes (VOL) from Etiope and Milkov (2004) and Patra et al. (2011). The time
series of the global total emissions and emissions from major sectors over 1980–2017 are shown in Figure 1a.
Anthropogenic and biomass burning emissions of other short‐lived species are also from the CEDS and
BB4CMIP databases and the SSP2‐4.5 scenario. Natural emissions of other short‐lived species are as described
by Naik et al. (2013). Biogenic emissions are calculated interactively following Guenther et al. (2006) as
described by Horowitz et al. (2020). The emissions for 13CH4 are described in Section 2.2.
The CH4 and 13CH4 sinks included in AM4.1 are mainly through the oxidation by OH, atomic chlorine (Cl), and
excited‐state atomic oxygen (O(1D)). Dry deposition of methane is also included in the model to mimic methane
loss by soil uptake. Detailed kinetic isotopic fractionations of 13CH4 are listed in Table S2 in Supporting
Information S1.
Similar to He2020, we include 12 additional methane tracers tagged by source sector to attribute methane from
agriculture
(CH4AGR), energy
(CH4ENE), industry
(CH4IND), transportation (CH4TRA),
residents
(CH4RCO), waste (CH4WST), shipping (CH4SHP), biomass burning (CH4BMB), ocean (CH4OCN), wetland
(CH4WET), termites (CH4TMI), and mud volcanoes (CH4VOL). The associated source‐tagged 13CH4 and full
Figure 1. Time series of methane emissions and isotopic source signatures. (a) Time series of global methane emissions from the initial inventories for major sectors on
the left Y axis and time series of emission‐weighted global mean δ13CH4 (olive) on the right Y axis; (b) same as (a) except time series of optimized global methane
emissions for major sectors on the left Y axis. Specific emission sectors include wetland (blue), agriculture (orange), energy (red), waste management (purple), biomass
burning (pink). The green line represents the sum of other smaller sources, including anthropogenic sectors (industry, residents, road transportation, and international
shipping) and natural sources (ocean, termites, and volcanoes), and the gray line represents total emissions. The dashed lines represent estimates from each experiment
(summarized in Table 1) and the shaded areas represent the upper and lower estimates from all experiments.
AGU Advances
10.1029/2025AV001822
HE ET AL.
3 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 4 ---
13CH4 tracers are also included. The tracers are emitted from the above listed sources, and undergo the same
chemical pathways, transport, and dry deposition as the full CH4 or 13CH4 tracer. For analysis, we combine
CH4IND, CH4TRA, CH4RCO, CH4SHP, and CH4OCN, CH4TMI, and CH4VOL as other tracers (i.e.,
CH4OTH). The same approach is applied to 13CH4 tracers.
After a 50‐year spin‐up run following the approach in He2020, several sets of simulations are conducted for
1980–2017 to quantify the methane budget and investigate the impacts of changes in methane sources and sinks
on atmospheric methane abundance (see Section 2.4). All model simulations are forced with prescribed
interannually‐varying sea surface temperatures and sea ice with the horizontal winds nudged to the National
Centers for Environmental Prediction (NCEP) reanalysis (Kalnay et al., 1996) as described in He2020.
2.2. Spatially Resolved Isotopic Signatures for Individual Methane Sources
Instead of using a single global mean isotopic ratio for each source sector, here we compile spatially resolved
δ13CH4 for major sectors as shown in Figure 2. For the agriculture (AGR) sector, we start from rice cultivation
and ruminant subsectors. Each subsector is associated with a specific global mean isotopic ratio. Specifically, for
the rice subsector, we apply country‐specific isotopic ratios based on Sherwood et al. (2017) and assume −63‰
for the rest of the world based on Whiticar and Schaefer (2007). For the ruminant subsector, considering the
different C‐3 and C‐4 vegetation types, we apply a global mean of −54.5‰ for C‐4 vegetation‐fed livestock and
−67.9‰ for C‐3 vegetation‐fed livestock based on Sherwood et al. (2017) along with the C‐4 fraction from Still
et al. (2009) to get spatially resolved isotopic signatures. We then get grid‐cell mean isotopic ratios for the AGR
sector by weighted‐averaging of country‐based emissions from the rice and ruminant subsectors from the CEDS
emission inventory. Similarly, for the energy (ENE) sector, we start from coal and oil and gas subsectors. We
apply country‐specific isotopic ratios based on Sherwood et al. (2017) for coal and oil and gas subsectors
Figure 2. Spatially resolved isotopic source signatures for agriculture (AGR, a), energy (ENE, b), biomass burning (BMB, c), and wetlands (WET, d). The isotopic
source signatures for agriculture are based on a weighted average of rice and ruminant subsectors. The isotopic source signatures for energy are based on a weighted
average of coal and oil and gas subsectors. The isotopic source signatures for biomass burning include the C3–C4 differential, and the isotopic source signatures for
wetlands are directly from Ganesan et al. (2018).
AGU Advances
10.1029/2025AV001822
HE ET AL.
4 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 5 ---
separately, and apply −41.2‰ for coal subsector and −44.6‰ for oil and gas subsector based on weighted mean
of Sherwood et al. (2017) for the rest of the world, where data is not available in Sherwood et al. (2017) for these
two subsectors. Then we obtain grid‐cell mean isotopic ratios for the ENE sector by weighted‐averaging of
country‐based emissions from coal and oil and gas subsectors from the CEDS emission inventory. For the WET
sector, we directly use the spatially resolved δ13CH4 from Ganesan et al. (2018). Strode et al. (2020) compared the
simulations using a global mean source signature for WET and using Ganesan et al. (2018), and found using
spatially varying source signature from Ganesan et al. (2018) can improve the interhemispheric gradient of
δ13CH4. However, uncertainties may still exist in Ganesan et al. (2018). For example, Oh et al. (2022) developed a
new map for spatially varying wetland δ13CH4, which seems to agree better with a few boreal and tropical sites
than Ganesan et al. (2018). We acknowledge the uncertainties of wetland δ13CH4 in Ganesan et al. (2018), and
need more observations to fully understand the spatial distributions of wetland δ13CH4. For the BMB sector, we
apply a global mean of −12‰ for C‐4 vegetation and −25‰ for C‐3 vegetation based on Lassey et al. (2007)
along with the C‐4 fraction from Still et al. (2009) to get spatially resolved isotopic signatures. For all other
sectors, each sector is associated with a specific global mean isotopic ratio. Then we update country‐specific
isotopic ratios based on Sherwood et al. (2017) for each sector with available observations and use global
mean ratios for regions where there are no observations. Detailed global mean ratios we used in this work are
summarized in Table S2 in Supporting Information S1. The time series of isotopic ratios of initial emissions are
shown in Figure 1a.
2.3. Leveraging Observations to Optimize Methane Emissions
We use measurements of CH4 and δ13CH4 from a globally distributed network of air sampling sites maintained by
the NOAA Global Monitoring Laboratory (GML) (Lan et al., 2024; Michel et al., 2023) for optimizing methane
emissions. We follow the same approach for emission optimization described in Ghosh et al. (2015) and He2020.
Specifically, we calculate the global and zonal averages of methane concentrations based on spatial and temporal
smoothing of CH4 measurements from multiple surface marine boundary layer (MBL) sites as in He2020. The
estimates of optimized emissions are based on comparison of simulated surface methane with NOAA GML MBL
observations and simulated methane isotopic signatures with global mean estimates from Schaefer et al. (2016)
for 1980–2014, assuming the same trend of δ13CH4 for 2015–2017 based on NOAA GML observations (Lan
et al., 2025). The observations used for emission optimization are shown in Table S3 in Supporting
Information S1.
In He2020, a simple mass balance approach is applied to optimize global total methane emissions with calculated
emission increment ΔE for each year. We do not optimize emissions for each grid cell as those in an inverse
modeling system. Instead, we uniformly scale emissions for specific sectors (as described below) globally for
each year by the ratio of the optimized emission total (Eopt = Einit + ΔE) to the initial emissions (Einit). In He2020,
several sensitivity simulations are conducted to investigate the source contributions through distributing ΔE into
either anthropogenic sectors or the wetland sector based on the sectoral source fraction in the initial inventories. In
this work, we apply an additional constraint from observed δ13CH4 to partition ΔE into individual source sectors
through 13CH4 emission optimization. A similar mass balance approach can also be applied to 13CH4 tracer as it is
explicitly simulated in the model. Based on the definition of isotopic ratios,
δ13C =
⎛
⎜⎜⎜⎜⎝
13C
12C
Rstd
−1
⎞
⎟⎟⎟⎟⎠
× 1,000
(1)
where Rstd = 0.0112372 from the Peedee belemnite (PDB) isotopic standard (Craig, 1957). We choose this
standard value to be consistent with the isotopic source signatures used in Table S2 in Supporting Information S1.
12C and 13C are concentrations of 12CH4 and 13CH4. We rewrite the and can get the difference in 13CH4 (Δ13C)
between simulated concentrations and observed concentrations as:
Δ13C = (δ13Csim −δ13Cobs
1,000
) × Rstd × 12Csim
(2)
AGU Advances
10.1029/2025AV001822
HE ET AL.
5 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 6 ---
where 12Csim is simulated global mean CH4 concentration, which should match the observed global means after
the optimization. Based on the mass balance:
dtB
dt = tE −
tL
(3)
we can rewrite the Equation 3 as:
ΔtE = H × d(ΔtC)
dt
+ S × ΔtC
(4)
tEopt = tEinit + ΔtE
(5)
where t could be either 12 or 13, representing either 12CH4 or 13CH4 tracer. H is burden (B)‐to‐concentration (C)
conversion factor and S is loss (L) factor, and both could be derived from the model simulations. Based on the
relationship of 13CH4 and 12CH4, we can also get burden and loss of 13CH4 as:
13B = Rsim × 12B
(6)
13L = ∑
n
i
12Li × αi × Rsim
(7)
where Rsim =
13Csim
12Csim, 12Li are the methane losses due to reactions with OH, O(1D), Cl, and soil uptake, αi =
13ki
12ki are
the isotopic fractionation factors for different loss processes, k is the rate coefficient of chemical reactions or
deposition velocity, and i represents each loss pathway.
For an optimized case, we can calculate δ13CEopt as
δ13CEopt =
⎛
⎜⎜⎜⎜⎜⎝
13Eopt
12Eopt
Rstd
−1
⎞
⎟⎟⎟⎟⎟⎠
× 1,000%
(8)
Meanwhile, δ13CEopt could be calculated as the emission‐weighted averages of individual source signatures:
δ13CEopt = ∑n
i=1 δ13CEi
12Ei
∑n
i=1
12Ei
(9)
where ∑n
i =1
12Ei = 12Eopt, and i represents the individual source sector. For an optimized case, we can get 13Bopt
and 13Lopt by replacing Rsim with Robs, 12B with 12Bopt, and 12L with 12Lopt and get 12Eopt and 13Eopt based on
Equations 4–7.
We need to iterate the model to get the best match of observed CH4 and 13CH4. Some of the previous studies
suggest biogenic sources are the dominant drivers for the post‐2006 methane increase (Oh et al., 2022; Schaefer
et al., 2016). In this work, we distribute ΔE into agriculture, wetland, and biomass burning emissions, considering
more depleted source signatures in the agriculture sector and wetland, and the large interannual variability of
wetland and biomass burning emissions. Specifically, an additional amount of 25 Tg yr−1 is added to the initial
CEDS AGR emissions for each year to bring it closer to AGR emissions in EDGARv5.0 (Monforti‐Ferrario
et al., 2019) and to match the observed isotopic ratios. Then we distribute the remaining ΔE into wetland
emissions (ΔEwet) and biomass burning emissions (ΔEbmb) constrained by the observed isotopic ratios. For the
AGU Advances
10.1029/2025AV001822
HE ET AL.
6 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 7 ---
optimized emissions, we keep the interannual variability of the initial emissions unchanged for all the sectors
except for wetland and biomass burning emissions.
2.4. Model Simulations With Sensitivity to Different Factors
We conduct several sets of model simulations for 1980–2017, as listed in Table 1, to quantify the methane budget
and the contributions of sources and sinks to the methane trend. The model simulation using the initial methane
emissions inventories (EXP0_NCEP) described in Section 2.1 is found to largely underestimate the methane
concentrations as shown in He2020. Here, we perform several optimization simulations that explore the sensi-
tivity of methane changes to uncertainties in methane emissions, kinetic fractionation of 13CH4 + OH, as well as
meteorological inputs that would affect OH levels, the dominant sink for methane.
Based on the initial results from EXP0_NCEP, we optimize agriculture, wetland, and biomass burning emissions
as discussed in Section 2.3, with EXP1 showing the optimized case driven by the NCEP reanalysis. Since we do
not optimize emissions regionally, this emission optimization largely relies on the spatial information from the
initial emission inventories, which are also associated with spatial and temporal uncertainty. Considering the
potential contributions from fossil fuel activities to the methane increase as discussed in previous studies (He
et al., 2020; Worden et al., 2017), we perform an additional simulation with energy sector from EDGAR v5.0
(EXP2) to compare with that from CEDS, as the EDGAR ENE tends to be lower than CEDS by about
25 ± 12 Tg yr−1 (lower bound of ENE in Figure 1b). In addition, the uncertainty in the kinetic isotopic frac-
tionation of 13CH4 + OH is also investigated in this work. We find a lower kinetic fractionation would require
negative BMB emissions in order to match the observed isotopic ratios. So we end up testing medium (EXP1) and
higher (EXP3) kinetic fractionation of 13CH4 + OH as shown in Table S2 in Supporting Information S1. Since
CH4 + OH is the major methane loss pathway, and the choice of meteorological fields affects OH as shown by He
et al. (2021), we perform additional simulations with different meteorological inputs from the Modern‐Era
Retrospective analysis for Research and Applications, Version 2 (MERRA‐2) (Gelaro et al., 2017), with
EXP0_MERRA2 and EXP4 driven by the initial emission inventories and optimized emissions, respectively.
3. Results and Discussions
3.1. Model Evaluation With Optimized Methane Emissions
Model simulations with optimized emissions show a clear latitudinal gradient of surface methane and δ13CH4,
with higher methane concentrations and more negative δ13CH4 in the Northern Hemisphere than the Southern
Hemisphere (Figure 3). There are no significant differences in the distributions and variations of methane and
δ13CH4 among EXP1, EXP3, and EXP4, as the anthropogenic emissions are identical across these simulations.
Due to different ENE emissions used in EXP1 (CEDS) and EXP2 (EDGAR), the major differences occur in
middle‐high Northern latitudes. Compared to EXP2, EXP1 shows overall better performance in capturing
methane trends and variabilities as well as δ13CH4 at regional scales, such as over BRW, MLG, and other sites in
Table 1
Model Simulations Conducted in This Work
Experiments
Description
EXP0_NCEP
Drive the model with NCEP reanalysis using compiled initial emission inventories for 1980–
2017
EXP0_MERRA2
Drive the model with MERRA2 reanalysis using compiled initial emission inventories for
1980–2017
EXP1
Drive the model with NCEP reanalysis; optimize methane emissions for AGR, WET, and
BMB sectors for 1980–2017 with compiled initial emission inventories for other sectors
EXP2
Same as EXP1, but replace the ENE sector in the CEDS with that from EDGAR v5.0; optimize
methane emissions for AGR, WET, and BMB sectors for 1980–2017
EXP3
Same as EXP1, but with higher fractionation for 13CH4 + OH; optimize methane emissions for
AGR, WET and BMB sectors for 1980–2017
EXP4
Same as EXP1, but drive the model with MERRA2 reanalysis; optimize methane emissions for
AGR, WET, and BMB sectors for 1980–2017
AGU Advances
10.1029/2025AV001822
HE ET AL.
7 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 8 ---
the Northern Hemisphere (Figure S1 in Supporting Information S1). In addition, all experiments can capture the
growth rates over MLO, CGO, and SPO sites (Figure S1 in Supporting Information S1).
We also aggregate the MBL sites into different latitude bands for evaluation (Figure 4). The observed surface
methane concentrations are higher and δ13CH4 is more negative in the Northern Hemisphere than the Southern
Hemisphere. Such latitudinal features are well captured by the model with optimized emissions (Figure 4), despite
the global‐scale emission optimization. Surface methane concentrations are reasonably well estimated across
different latitude bands, although the model exhibits a high bias (<20 ppb) over tropics, and the low bias (about 22
ppb) over high latitudes (53.1–90°N and 53.1–90°S). In addition, the methane trends are well captured by the
model, with the correlation coefficient (R2) > 0.9 across different latitude bands. Meanwhile, the model is also
able to capture the global trend of δ13CH4 since 1998, with mean bias = −0.07 and R2 > 0.92 (Figure 4a). The
model can reproduce observed magnitudes and trends of δ13CH4 generally well in the tropics and Southern
Hemisphere, but shows larger low bias in the temperate Northern Hemisphere and poor temporal correlation over
the northern high latitudes. However, the bias has been reduced and the correlation has improved since 2010. This
is likely due to much fewer observational sites for δ13CH4 in the early 2000s, which may not fully represent the
temperate and polar Northern Hemisphere conditions, where there are more complex emission sources than those
in the Southern Hemisphere.
Since selected MBL observations represent the background conditions, there are not many discrepancies among
four different experiments across different latitude bands. However, EXP2 shows higher model bias than other
experiments especially over the polar and temperate Northern Hemisphere (Figures 4c and 4e). The differences
between CEDS ENE and EDGAR ENE are partly driven by different estimates of coal mining over China (Hoesly
et al., 2018; Höglund‐Isaksson et al., 2020; Oreggioni et al., 2021; Saunois et al., 2025; Solazzo et al., 2021). For
example, WLG is a remote site located in western China, where the methane concentrations have shown to be
Figure 3. Time series of latitudinal distribution of surface annual methane (left column, panels (a) & (c)) and δ13CH4 (right column, panels (b) & (d)) from EXP1 (upper
row) and EXP2 (lower row). Circles represent National Oceanic and Atmospheric Administration Global Monitoring Laboratory observations of annual mean methane
and δ13CH4 over five different sites. From North to South: Barrow, USA (BRW, 71.3°N, 156.6°W); Mountain Waliguan, China (MLG, 36.3°N, 100.9°E); Mauna Loa,
USA (MLO, 19.5°N, 155.6°W); Cape Grim, Australia (CGO, 40.7°S, 144.7°E); South Pole, USA (SPO, 90.0°S, 24.8°W).
AGU Advances
10.1029/2025AV001822
HE ET AL.
8 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 9 ---
affected by the long‐range transport from source regions (Liu et al., 2021). The comparisons of methane con-
centrations and δ13CH4 at WLG (Figure S1 in Supporting Information S1) suggest overall better emission es-
timates and source contributions in EXP1 (CEDS) than EXP2 (EDGAR). Satellite evaluation of column‐averaged
CH4 concentrations over East Asia (Figure S2 in Supporting Information S1) further confirms better ENE esti-
mates from EXP1 (CEDS) than EXP2 (EDGAR) in the Northern Hemisphere.
3.2. Optimized Global Methane Budget
We focus on the optimized global methane budget during four time periods (i.e., 1980–1989, 1990–1998, 1999–
2006, and 2007–2017) to be consistent with the changes in the methane growth in the past decades. As shown in
Figure 5a and Table 2, the optimization results in the multi‐year mean total methane emissions of
521 ± 14 Tg yr−1 during 1980–1989, 555 ± 15 Tg yr−1 during 1990–1998, 568 ± 13 Tg yr−1 during 1999–2006,
and 607 ± 11 Tg yr−1 during 2007–2017, with associated multi‐year mean methane sinks of 486 ± 19 Tg yr−1,
536 ± 12 Tg yr−1, 566 ± 8 Tg yr−1, and 589 ± 8 Tg yr−1, respectively. Those estimates are within the ranges of
estimates in the previous studies using either top‐down or bottom‐up approaches (Saunois et al., 2020, 2025). The
optimized global methane budget does not vary across simulations EXP1‐3 (Table 1) as they are all constrained by
the same meteorology and methane observations. Forced by different meteorology from MERRA2, the global
methane emissions and sinks are slightly higher in EXP4 by 7–15 Tg yr−1 during different growth periods
(Table 2) than EXP1‐3, which is mainly due to higher OH levels in the MERRA2‐driven simulations than in the
NCEP‐driven simulations. He2020 using the GFDL‐AM4.1 model suggested a 1% change in OH could lead to
about 4 Tg yr−1 change in the optimized methane emissions. The responses of OH levels to the different
meteorological inputs have been discussed in our previous work of He et al. (2021). In summary, there is a
significant increase in the multi‐year mean methane emissions from 1980 to 1989 to 1990–1998 (by 30 Tg yr−1),
followed by a smaller increase in 1999–2006 (by 13 Tg yr−1) and rebounded emissions in 2007–2017 (by
40 Tg yr−1 in EXP1‐3 or by 34 Tg yr−1 in EXP4).
All experiments show similar changes in the global multi‐year mean source δ13CH4 and sink fractionation in the
past decades as shown in Table 2. Specifically, there is a 0.6‰ decrease in global multi‐year mean source δ13CH4
from the 1980s to the 1990s, followed by minor changes from the 1990s to 1999–2006 (<0.1‰) and an increase
Figure 4. Latitudinal comparisons of methane concentrations and atmospheric δ13CH4 from National Oceanic and Atmospheric Administration Global Monitoring
Laboratory observations (gray) and four experiments (EXP1 in blue, EXP2 in orange, EXP3 in green and EXP4 in brown). Each panel (a–f) shows methane evaluation
on the left and atmospheric δ13CH4 evaluation on the right, with circles representing monthly mean within each latitude band. Mean bias and square of correlation
coefficient (R2) are shown for each model evaluation in corresponding colors. We process the global mean and latitudinal mean δ13CH4 following the same approach for
global mean CH4 concentrations as done in He2020 based on the measurements done by the Institute of Arctic and Alpine Research (INSTAAR) (Michel et al., 2023), to
allow for fair comparisons between observations and model simulations.
AGU Advances
10.1029/2025AV001822
HE ET AL.
9 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 10 ---
of 0.2–0.3‰ from 1999 to 2006 to 2007–2017. Similarly, there is a 0.2‰ decrease in global multi‐year mean sink
fractionation from the 1980s to the 1990s, followed by an increase of 0.1 ‰ from the 1990s to 1999–2006 and an
increase of 0.1 ‰ from 1999 to 2006 to 2007–2017. With higher isotopic fractionation for 13CH4‐OH sink in
EXP3 than EXP1‐2, there is about 0.6 ‰ difference in the global multi‐year mean source δ13CH4 and sink‐
weighted fractionation. On the other hand, different meteorology (EXP1 vs. EXP4) shows minor impacts
(<0.1 ‰) on both optimized source signatures and sink‐weighted fractionations.
Both methane sources and sinks increased from 1999 to 2006 to 2007–2017. The estimated methane emission
increase is higher than that by Basu et al. (2022) using an inversion modeling framework with both methane and
δ13CH4 constraints, where methane loss rates in the stratosphere are prescribed and tropospheric losses due to Cl
and OH are simulated based on prescribed Cl and OH levels. In our model, we explicitly simulate methane losses
due to OH, Cl, and O(1D) throughout the atmosphere. Such differences lead to different estimates in methane
sinks and therefore different optimized methane emissions. Our larger emission increase is required to offset the
higher methane sinks due to the increasing OH levels simulated by our model (He et al., 2020, 2021) in order to
match the observations. Due to the increasing trend in methane and OH levels, post‐2006 methane sinks have
increased by 23 Tg yr−1 in EXP1‐3 and 19 Tg yr−1 in EXP4, compared with 1999–2006 (Table 2). As shown in
Table 2, the optimization suggests an increase of about 0.24–0.29 ‰ in the global multi‐year mean source δ13CH4
from 1999 to 2006 to 2007–2017. The post‐2006 shift of the global multi‐year mean source δ13CH4 is larger than
that in Schaefer et al. (2016), however, in an opposite direction as that in other works (Chandra et al., 2024; Ghosh
et al., 2015; Thanwerdas et al., 2024). This is likely due in part to the different representations of methane sinks
(e.g., OH trend) and isotopic fractionations between this work and their studies. We calculate the sink‐weighted
average fractionation factor, which shifts from −6.32 ± 0.05‰ in 1999–2006 to −6.20 ± 0.02‰ in 2007–2017 in
EXP1 (Table 2). The calculated sink fractionation factor is more comparable to the mean value in Schwietzke
et al. (2016) but much larger than the default value of −7.85 ‰ in Lan, Basu, et al. (2021). In a higher OH sink
fractionation case (EXP3), the sink‐weighted average fractionation factor shifts from −5.70 ± 0.05 ‰ in 1999–
2006 to −5.57 ± 0.02 ‰ in 2007–2017. This factor is closer to the 90th percentile of the range in Schwietzke
et al. (2016). The different OH sink fractionations (median sink vs. high sink) could lead to 0.62 ‰ difference in
the total sink fractionation factor. To account for such a difference, we need to reduce the wetland emissions in
EXP1 by about 10 Tg yr−1 and transfer this amount to biomass burning emissions in EXP3 in order to match the
observations (Figure S3 in Supporting Information S1).
Figure 5. Global methane budget (a) and isotopic source signature and fractionation (b) during 1980–2017 for different growth periods based on EXP1. (a) Each bar
represents the multi‐year mean of individual sources (positive) or sinks (negative) with the net as the imbalance, which are shown on the left Y axis. Black dots represent
observed global monthly mean CH4 with the solid magenta line representing simulated values, which are shown on the right Y axis; (b) Each bar represents the multi‐
year mean of source‐weighted isotopic ratios (red) or sink‐weighted fractionation (blue), which are shown on the left Y axis. Black dots represent global annual δ13CH4
from Schaefer et al. (2016), with the solid magenta line representing simulated values, which are shown on the right Y axis.
AGU Advances
10.1029/2025AV001822
HE ET AL.
10 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 11 ---
3.3. Possible Drivers for the Post‐2006 Methane Growth
Although both methane sources and sinks are higher during 2007–2017 than 1999–2006, the increase in the total
methane sources dominates over the methane sinks, leading to a net increase in the atmospheric methane
abundances, driving the post‐2006 methane growth. Figure 6 shows the changes of methane emissions and source
δ13CH4 from 1999 to 2006 to 2007–2017 across different latitude bands. Emissions from AGR and waste tracer
(WST) in 2007–2017 are generally higher over most of the regions except high northern latitudes. These emission
differences are directly based on the CEDS inventory. Both CEDS (EXP1) and EDGAR v5.0 (EXP2) experiments
show increases in fossil fuel emissions across different latitude bands except for a small decrease in the high
Table 2
Optimized Global Methane Budget, Source‐Weighted Signatures, and Sink‐Weighted Fractionation (Multi‐Year Global
Mean ± Standard Deviation)
Period
Runs
Sources (Tg yr−1)
Total
AGR + WST
ENE
WET
BMB
1980–1989
EXP1
521 ± 14
184 ± 5
104 ± 3
158 ± 9
25 ± 5
EXP2
92 ± 7
166 ± 10
29 ± 5
EXP3
104 ± 3
149 ± 9
34 ± 4
EXP4
536 ± 15
170 ± 9
27 ± 5
1990–1998
EXP1
555 ± 15
197 ± 2
106 ± 3
184 ± 9
17 ± 6
EXP2
90 ± 2
193 ± 10
25 ± 7
EXP3
106 ± 3
175 ± 9
25 ± 7
EXP4
566 ± 16
193 ± 11
19 ± 7
1999–2006
EXP1
568 ± 13
206 ± 5
120 ± 10
180 ± 10
12 ± 5
EXP2
88 ± 6
197 ± 9
27 ± 4
EXP3
120 ± 10
171 ± 10
21 ± 5
EXP4
580 ± 11
190 ± 10
15 ± 5
2007–2017
EXP1
607 ± 11
225 ± 6
150 ± 6
177 ± 7
5 ± 5
EXP2
111 ± 8
196 ± 8
25 ± 5
EXP3
150 ± 6
168 ± 7
15 ± 6
EXP4
614 ± 11
183 ± 7
5 ± 6
Period
Runs
Sinks (Tg yr−1)
Source‐weighted signature (‰)
Sink‐weighted fractionation (‰)
Total
OH
1980–1989
EXP1
486 ± 19
430 ± 14
−54.72 ± 0.27
−6.21 ± 0.09
EXP2
EXP3
−54.05 ± 0.31
−5.59 ± 0.09
EXP4
500 ± 20
443 ± 15
−54.69 ± 0.28
−6.16 ± 0.08
1990–1998
EXP1
536 ± 12
468 ± 12
−55.32 ± 0.37
−6.43 ± 0.02
EXP2
EXP3
−54.73 ± 0.36
−5.81 ± 0.02
EXP4
548 ± 13
480 ± 13
−55.28 ± 0.39
−6.37 ± 0.02
1999–2006
EXP1
566 ± 8
501 ± 9
−55.25 ± 0.20
−6.32 ± 0.05
EXP2
EXP3
−54.64 ± 0.20
−5.70 ± 0.05
EXP4
577 ± 6
512 ± 7
−55.19 ± 0.20
−6.27 ± 0.04
2007–2017
EXP1
589 ± 8
526 ± 8
−54.96 ± 0.24
−6.20 ± 0.02
EXP2
EXP3
−54.37 ± 0.24
−5.57 ± 0.02
EXP4
596 ± 8
533 ± 7
−54.95 ± 0.24
−6.17 ± 0.02
AGU Advances
10.1029/2025AV001822
HE ET AL.
11 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 12 ---
northern latitudes in EDGAR v5.0. Also, the increases in fossil fuel emissions are overall lower in EDGAR v5.0
than in CEDS. The optimized wetland emissions decrease in the tropics and the Northern Hemisphere, with
smaller increases in the Southern Hemisphere middle latitudes, while the optimized biomass burning emissions
Figure 6. Changes of methane emissions (left column, a–d) and source δ13CH4 (right column, e–h) from 1999–2006 to 2007–2017 across different latitude bands from
four experiments (row1: EXP1, row2: EXP2, row3: EXP3, and row4: EXP4). Different colors represent changes from different sources, including agriculture (AGR,
orange), waste (WST, purple), biomass burning (BMB, pink), energy (ENE, red), and wetland (WET, blue). Gray bars represent the changes from total methane
emissions and source δ13CH4.
AGU Advances
10.1029/2025AV001822
HE ET AL.
12 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 13 ---
decrease across all the latitude bands. As a result, there are minor decreases in global wetland emissions
(<3 Tg yr−1 in EXP1‐3 and 7 Tg yr−1 in EXP4, or by <4%), but moderate‐to‐large decreases in biomass burning
emissions (−2 to −8 Tg yr−1 or by 8%–57%) from 1999 to 2006 to 2007–2017. While Saunois et al. (2025)
showed small increases in wetland emissions from 2000 to 2009 to 2010–2019 (<7 Tg/yr or within 5%), the wide
spread of bottom‐up emission estimates are observed due to different model parameterizations. For example, the
very small decreases in wetland emissions estimated in this work are consistent with an independent bottom‐up
estimate by McNicol et al. (2023), which suggested a 3 Tg/yr decrease from 2001 to 2006 to 2007–2017. A small
decline in wetland emissions after 2010 is also consistent with another bottom‐up estimate by Xiao et al. (2024).
Lower wetland and biomass burning emissions post‐2006 than those in 1999–2006 are consistent with findings in
previous studies (Thanwerdas et al., 2024; Worden et al., 2017), but inconsistent with some studies that suggested
higher wetland emissions (Chandra et al., 2024), possibly due in part to the different model representations of the
processes that affect the methane cycle. The increases in emissions from agriculture, waste management, and
fossil fuels after 2006 are generally consistent with those in previous studies (Jackson et al., 2020; Thanwerdas
et al., 2024).
All experiments show an overall decrease in the source δ13CH4 (more negative) over the tropics and the Southern
Hemisphere, with an overall increase (less negative) over middle and high latitudes of the Northern Hemisphere
(right column in Figure 6). The decreases of source δ13CH4 over the tropics and the Southern Hemisphere are
driven by the decreases in the 13C‐enriched BMB emissions and increases in the 13C‐depleted AGR and WST
emissions. The increases of source δ13CH4 over middle and high latitudes of the Northern Hemisphere are driven
by the increases in the ENE emissions, which also drive the increases in global mean source δ13CH4. However, as
the global mean atmospheric δ13CH4 shifts toward more negative values, considering much larger emission
changes and relatively higher OH levels over the tropics than over Southern Hemisphere middle and high latitudes
(Figure S4 in Supporting Information S1), the post‐2006 shift of atmospheric δ13CH4 is more likely due to the
increases in the tropical 13C‐depleted AGR and WST emissions with decreases in the 13C‐enriched BMB
emissions. Sensitivity simulations with different sink fractionations and different meteorology show a similar
shift of the latitudinal mean source δ13CH4. However, with different ENE emissions in EXP1 and EXP2, much
larger impacts occur over tropics and the Southern Hemisphere, which are associated with different changes in the
WET, BMB, and ENE emissions.
Changes in the methane sinks and the isotopic fractionation due to OH trend may also contribute to the δ13CH4
shift after 2006, particularly because there is a net change in the global mean atmospheric δ13CH4 that shifts
toward more negative values (13C‐depleted) with the global mean source δ13CH4 shifting in an opposite direction.
This finding is partly consistent with that from Skeie et al. (2023) indicating that decrease in δ13CH4 between
2008 and 2014 can be explained by increases in OH levels. However, this is inconsistent with previous studies
based on prescribed methane sinks or OH levels (Basu et al., 2022; Chandra et al., 2024). As OH is explicitly
simulated in our model, changes in the methane concentrations will feed back on the OH levels, which further
affect methane sinks, isotopic fractionation, and therefore methane lifetime. We discuss this in the following
Section (3.4).
To further understand the changes in the rate of atmospheric methane increase, we follow the same approach used
by He2020 to calculate the linear trend of each source‐tagged tracers over the background sites used in calculating
background methane concentrations by NOAA GML (Figure 7). As shown in Figure 7, all experiments show the
global total tracer trend during 2007–2017 is dominated by the fossil fuel tracer CH4ENE, followed by the
biogenic tracers CH4AGR and CH4WST. All the trends are calculated based on the global averages in the MBL.
We also calculate the trends across different latitudes (Figure S5 in Supporting Information S1), which do not
show much difference in the observed methane trends considering the well‐mixed background conditions.
Compared to 1999–2006, the increasing trends of CH4AGR and CH4ENE are significantly higher in 2007–2017,
which are associated with higher AGR and ENE emissions. Another widely used methane fossil fuel emissions
estimated from the Greenhouse Gas and Air Pollution Interactions and Synergies (GAINS) are generally within
the range of EDGAR and CEDS estimates and show smaller post‐2006 increase than EDGAR and CEDS
(Höglund‐Isaksson et al., 2020). He2020 showed a 3 ppb yr−1 increase of post‐2006 CH4ENE even with ENE
emissions kept constant after 2006. Therefore, if GAINS ENE emissions were used, there would be an increase of
post‐2006 CH4ENE larger than 3 ppb yr−1 but smaller than 7 ppb yr−1 as estimated from CEDS in this work.
Meanwhile, there is a larger decreasing trend of CH4WET in EXP1, 3, and 4, despite minor decreases in WET
emissions. This is mainly due to higher OH levels in 2007–2017 that further decrease CH4WET concentrations.
AGU Advances
10.1029/2025AV001822
HE ET AL.
13 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 14 ---
More interestingly, there is a change from an increasing trend of CH4WET in 1999–2006 to a decreasing trend of
CH4WET in 2007–2017 in EXP2, while there is only about 1 Tg yr−1 difference in WET emissions between the
two periods, further demonstrating the critical role of OH in affecting methane trends. Our earlier work (He2020)
found that for wetland emissions to be the dominant driver of methane growth, there would need to be a sig-
nificant and sustained increase in the post‐2006 wetland emissions, alongside with concurrent decreases in the
anthropogenic emissions, which is a less likely scenario. The uncertainties in the spatial distributions of wetland
δ13CH4 will not affect the overall conclusion of this work but may impact the regional changes in the δ13CH4.
Figure 7. Linear trend of source‐tagged methane tracers during different growth periods from all the four experiments. Gray bars represent observed total methane trend
and black bars represent model simulated methane trend, with other color bars representing trends of source‐tagged methane tracers, including agricultural tracer, waste
tracer, wetland tracer, energy tracer, biomass burning tracer, and tracer from other sources.
AGU Advances
10.1029/2025AV001822
HE ET AL.
14 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 15 ---
Similarly, higher OH levels and lower BMB emissions lead to a larger decreasing trend of CH4BMB in 2007–
2017. Despite WST emissions being higher in 2007–2017, the trend of CH4WST is slightly smaller than that in
1999–2006, resulting from higher sinks of CH4WST (due to higher OH levels). There is also a smaller decreasing
trend of CH4OTH in 2007–2017, mainly due to higher emissions from other anthropogenic sources, however, not
large enough to offset the higher sinks. In summary, the emission increase has to be large enough to offset the sink
increase (due to the OH increase simulated by the model) to lead to a positive (increasing) tracer trend. As a result,
the increasing trends of CH4AGR and CH4ENE drive the post‐2006 growth of total methane (CH4TOT).
3.4. CH4‐OH Feedback and Tropospheric Lifetime
Increasing methane emissions and therefore concentrations would lead to decreases in OH levels (Figure 8a). There
is a 1.9% decrease in the tropospheric OH levels in the simulations driven by the optimized emissions (EXP1)
versus initial emissions using NCEP meteorology (EXP0_NCEP) and a 2.5% decrease in the tropospheric OH
levels using MERRA2 meteorology (EXP4 vs. EXP0_MERRA2). There is a noticeable feedback on OH levels
with higher methane emissions. Lower OH levels tend to increase tropospheric methane lifetime as shown in
Figure 8b. Compared to the simulations with initial emissions, simulations with optimized emissions increased
methane lifetime by 0.2 years forced with NCEP meteorology and by 0.3 years forced with MERRA2 meteorology.
There is an overall decreasing trend in methane lifetime since 1980 until it becomes relatively stable during 2006–
2011. All the experiments show a lower lifetime in 2007–2017 (9.50 ± 0.19 yr) than 1999–2006 (9.74 ± 0.23 yr).
The changes in the tropospheric methane lifetime are partly driven by the OH trend (Figure 7a). The model
simulated OH concentrations and trends in this work are comparable with the previous studies using other
chemical transport models (Zhao et al., 2019). Previous studies also found the model simulated OH trend to be
driven by the emission ratios of nitrogen oxides and carbon monoxide in the chemical transport models (Dalsoren
et al., 2016; Skeie et al., 2023). Therefore, it is important to better constrain the emission trends to reduce the
uncertainty in the simulated OH trend.
We then calculate the methane feedback factor following Holmes (2018), which gives a 1980–1989 average of
1.288 ± 0.028, 1990–1998 average of 1.359 ± 0.006, 1999–2006 average of 1.383 ± 0.005 and 2007–2017 average
of 1.404 ± 0.002 across different experiments. These values are comparable to the present‐day values calculated in
the previous studies (Heimann et al., 2020; Holmes, 2018). Holmes (2018) suggested the feedback factor increased
as a function of methane burden from preindustrial times and reached a plateau under the present‐day conditions. In
this work, we still see a continuous but small increase in the feedback factor since the 1980s. Higher feedback factor
suggests that emission perturbations on atmospheric methane concentrations would persist longer. In other words,
there is an increasing sensitivity from an emission increase on methane concentrations and lifetime. This is
particularly important when assessing the responses of methane concentrations to the emission changes.
Figure 8. Time series of simulated tropospheric OH levels (a) and tropospheric methane lifetime (b). Dashed lines represent model simulations with initial emissions
(EXP0) and solid lines represent model simulations with optimized emissions (EXP1 and EXP4). Blue lines represent results from NCEP‐driven simulations and orange
lines represent results from MERRA2‐driven simulations.
AGU Advances
10.1029/2025AV001822
HE ET AL.
15 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 16 ---
4. Conclusions
In this work, we constrain a global chemistry‐climate model with methane and isotopic observations to under-
stand changes in the global methane budget. We apply spatially‐resolved isotopic signatures instead of a single
global mean value to better constrain the methane sources. Unlike many other studies that rely on prescribed
methane sinks or climatological OH concentrations, our model includes comprehensive atmospheric chemistry to
interactively simulate OH concentrations and trends, as well as the CH4‐OH feedback. Several model simulations
have been performed to attribute the source contribution to the methane increase over the past several decades.
While anthropogenic activities are found to be mainly responsible for the methane increase since the 1980s, the
increasing OH trend simulated by the model plays a critical role in the global methane evolution.
We find the increases in tropical 13C‐depleted agricultural and waste emissions and decreases in 13C‐enriched
biomass burning emissions, along with increasing OH, contribute to the post‐2006 observed shift of atmo-
spheric δ13CH4 toward more negative values. Due to the increasing OH trend simulated by our model, the in-
crease in methane emissions from a specific source sector does not always lead to increasing concentrations of the
corresponding source‐tagged methane tracer. As a result, the post‐2006 methane growth is more likely to be
driven by increasing agriculture and fossil fuel emissions, which are large enough to offset the increasing sinks.
Our study highlights the critical role of OH and methane sinks when interpreting the recent changes in methane
growth. Neglecting changes in OH could possibly lead to misinterpreting emission changes with respect to the
long‐term observations of background methane and δ13CH4 (Rigby et al., 2017). In addition, our study reveals the
importance of the CH4‐OH feedback, which must be considered when assessing responses of methane concen-
trations to the emission changes.
Sensitivity simulations using different ENE emissions (CEDS vs. EDGAR), different isotopic fractionations, and
different meteorology do not change the overall conclusion, but can lead to 9–13 Tg yr−1 differences in the
optimized WET emissions and 2–12 Tg yr−1 differences in the optimized BMB emissions. However, the different
estimates in WET and BMB emissions resulting from different isotopic fractionations and meteorology do not
have significant impacts on the post‐2006 shift of regional source δ13CH4, while noticeable impacts from different
ENE emissions are shown across different latitude bands. We acknowledge the uncertainties in the spatial dis-
tributions of methane emissions. We optimize global emission totals instead of grid‐level emissions as is
commonly done in an inverse modeling system, which may affect the estimates of emission changes regionally.
There is possible uncertainty in the individual isotopic source signatures used in this work in terms of spatial and
temporal variability, which can impact regional δ13CH4 (Feinberg et al., 2018). Model uncertainties along with
emission inputs could also lead to uncertainties in the simulated OH levels. We rely heavily on the observations of
methane and its isotopic composition to constrain and validate the model, and interpret the results. Therefore,
continued observations of methane concentrations and isotopic signatures are necessary to improve our under-
standing of the changes in the global methane budget.
Conflict of Interest
The authors declare no conflicts of interest relevant to this study.
Data Availability Statement
NOAA GML CH4 and δ13CH4 observations can be downloaded at https://gml.noaa.gov/aftp/data/trace_gases/
ch4/flask/ and https://gml.noaa.gov/aftp/data/trace_gases/ch4c13/flask/.
Model data can be accessed through Zenodo at https://doi.org/10.5281/zenodo.17487837.
References
Basu, S., Lan, X., Dlugokencky, E., Michel, S., Schwietzke, S., Miller, J. B., et al. (2022). Estimating emissions of methane consistent with
atmospheric measurements of methane and δ13C of methane. Atmospheric Chemistry and Physics, 22(23), 15351–15377. https://doi.org/10.
5194/acp‐22‐15351‐2022
Bloom, A. A., Bowman, K. W., Lee, M., Turner, A. J., Schroeder, R., Worden, J. R., et al. (2017). A global wetland methane emissions and
uncertainty dataset for atmospheric chemical transport models (WetCHARTs version 1.0). Geoscientific Model Development, 10(6), 2141–
2156. https://doi.org/10.5194/gmd‐10‐2141‐2017
Brasseur, G. P., Hauglustaine, D. A., Walters, S., Rasch, P. J., Muller, J. F., Granier, C., & Tie, X. X. (1998). MOZART, a global chemical
transport model for ozone and related chemical tracers 1. Model description. Journal of Geophysical Research, 103(D21), 28265–28289.
https://doi.org/10.1029/98jd02397
Acknowledgments
This work was initiated at Princeton
University, supported by the Carbon
Mitigation Initiative at Princeton
University (Grant 02085(7)). Part of the
research was done at the University of
Colorado Boulder, supported by the
NOAA Cooperative Agreement
(NA22OAR4320151), for the Cooperative
Institute for Earth System Research and
Data Science (CIESRDS). We thank the
GFDL model development team for
developing the ESM4.1/AM4.1. We thank
NOAA GML for providing the surface
methane observations. We thank the
Institute of Arctic and Alpine Research
(INSTAAR) at the University of Colorado
for the methane isotopic measurements.
We also thank Xin Lan from NOAA GML
and Cooperative Institute for Research in
Environmental Sciences at University of
Colorado Boulder and Sylvia Englund
Michel from INSTAAR at University of
Colorado Boulder for insightful
discussion. We also thank the two
anonymous reviewers for their comments
and feedback. The statements, findings,
conclusions, and recommendations are
those of the author(s) and do not
necessarily reflect the views of NOAA or
the U.S. Department of Commerce.
AGU Advances
10.1029/2025AV001822
HE ET AL.
16 of 19
 2576604x, 2026, 1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025AV001822 by Nanjing University, Wiley Online Library on [03/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
