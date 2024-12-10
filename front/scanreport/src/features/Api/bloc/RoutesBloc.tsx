import { Container, Divider, Grid, Typography } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { Routes } from "../ApiType";
import { colors } from "features/colors";

interface RoutesProps {
  route: Routes;
}



const RoutesBloc: FC<RoutesProps> = ({ route }) => {
  const dispatch = useDispatch();

  return (
    <Container>
      <Grid container style={{
        backgroundColor: '#fff', // Background color
        borderRadius: '4px', // Border radius
        marginBottom: '16px', // Margin bottom
        padding: '16px', // Padding
        display: 'flex',
        flexDirection: 'column',
        boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)', // Box shadow
      }}>
        <Typography variant="h6" style={{ fontSize: '16px', fontWeight: 'bold', marginBottom: '8px' }}>
          {route.path}
        </Typography>
        <Typography variant="body2" style={{ color: '#999' }}>
          Methods: {route.methods}
        </Typography>
        <Typography variant="body2" style={{ color: '#999' }}>
          endpoint: {route.endpoint}
        </Typography>
        <Typography variant="body2" style={{ color: '#999' }}>
          Parameters: {route.params ? JSON.stringify(route.params) : '-'}
        </Typography>
        <Typography variant="body2" style={{ color: '#999' }}>
          View Function: {route.view_func || '-'}
        </Typography>
      </Grid>
      <Grid item xs={12}>
        <Grid item mb={2} xs={12}>
          <Divider sx={{ backgroundColor: colors.primary }} />
        </Grid>
      </Grid>
    </Container>
  );
}

export default RoutesBloc;
