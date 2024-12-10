import { Button, Divider, Grid, LinearProgress, Typography } from "@mui/material";
import { colors } from "features/colors";
import React, { useEffect, FC } from "react";

interface AnalyseProps {
  libelleTxt: string;
  libelleBtn: string;
  stateAnalyse: number;
  divider: boolean;
  fctClick: () => void;
}

const AnalyseBloc: FC<AnalyseProps> = ({ libelleTxt, libelleBtn, stateAnalyse, divider, fctClick }) => {

  useEffect(() => {
    //
  }, []);

  return (
    <Grid container alignItems="center">
      <Grid container alignItems="center" mt={2}>
        <Grid item xs={2} >
          <Typography variant="body1" sx={{ fontFamily: "Roboto" }} align="left" my={2} gutterBottom >
            {libelleTxt + " :"}
          </Typography>
        </Grid>
        <Grid item xs={4} style={{ textAlign: 'center' }}>
          <Button variant="outlined" disabled={stateAnalyse === 1} color="warning" size="small" onClick={fctClick}>
            {libelleBtn}
          </Button>
        </Grid>
        {stateAnalyse !== 0 && (
          <Grid item xs={6}>
            <Grid container alignItems="center" textAlign={"center"} justifyContent="center" justifyItems="center">
              <Grid item xs={12} style={{ textAlign: 'center' }}>
                <LinearProgress color={stateAnalyse === 2 ? "info" : "warning"} variant={stateAnalyse === 2 ? "determinate" : "indeterminate"} value={100} />
              </Grid>
              <Grid item xs={12} >
                <Typography variant="body1" sx={{ fontFamily: "Roboto" }} align="center" my={2} gutterBottom >
                  {stateAnalyse === 2 ? "Terminé ": "En cours"}
                </Typography>
              </Grid>
            </Grid>
          </Grid>
        )}
      </Grid>
      {divider && (
        <Grid item mb={2} xs={12}>
          <Divider sx={{ backgroundColor: colors.primary, opacity: 0.6 }} />
        </Grid>
      )}
    </Grid>

  );
}

export default AnalyseBloc;
