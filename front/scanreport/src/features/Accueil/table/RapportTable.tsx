import React from "react";
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  IconButton,
} from "@mui/material";
import { Edit, Delete, Launch } from "@material-ui/icons";
import { Rapport } from "../RapportType";

interface RapportTableProps {
  rapports: Rapport[];
  openRapport: (rapport: Rapport) => void;
  onDelete: (rapport: number) => void;
}

const RapportTable = (props: RapportTableProps) => {
    const { rapports, onDelete,openRapport } = props;
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Nom</TableCell>
            <TableCell>Création</TableCell>
            <TableCell>Fichier</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Ouverture</TableCell>
            <TableCell>Suppression</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rapports.map((rapport) => (
            <TableRow key={rapport.id}>
              <TableCell>{rapport.name}</TableCell>
              <TableCell>{rapport.created_at}</TableCell>
              <TableCell>{rapport.format}</TableCell>
              <TableCell>{rapport.type}</TableCell>
              <TableCell>
                <IconButton color="primary" onClick={() => openRapport(rapport)}>
                  <Launch />
                </IconButton>
              </TableCell>
              <TableCell>
                <IconButton color="error" onClick={() => onDelete(rapport.id)}>
                  <Delete />
                </IconButton>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default RapportTable;
