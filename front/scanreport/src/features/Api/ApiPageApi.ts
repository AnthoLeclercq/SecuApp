import { fetchApi } from "features/rest";
import { toast } from "react-toastify";
import { Routes } from "./ApiType";

export const getRoutes = (funcSuccess: (data: Routes[]) => void) => async (dispatch: any) => {
  try {
    fetchApi({
      method: 'GET',
      endpoint: '/routes',
      funcSuccess: (data) => {
        funcSuccess(data.routes);
      },
      dispatch
    });
  } catch (err) {
    toast.error('Une erreur s\'est produite. Veuillez réessayer.');
  }
};
