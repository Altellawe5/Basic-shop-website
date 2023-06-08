import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Axios from "axios";
import ProductContainer from "../components/ProductContainer";
import Header from "../components/Header";
import VerticalNavBar from "../components/VerticalNavBar";
import Footer from "../components/Footer";
import Style from "./HomePage.module.css"

const SearchPage = () => {
    const { term } = useParams();
    const [producten, setProducten] = useState([]);
    useEffect(() => {
        const fetchProducten = async () => {
            try {
                const response = await Axios.get(
                    `http://localhost:8000/api/products/search/?q=${term}`
                );
                setProducten(response.data);
            } catch (error) {
                console.log(error);
            }
        };

        fetchProducten();
    }, [term]);
    return (
        <>
            <VerticalNavBar />
            <div className={Style.mainBody}>
                <Header />
                <ProductContainer
                    categorie={`Resultaat voor: ${term}`}
                    producten={producten}
                />
                <Footer />
            </div>
        </>

    );
};

export default SearchPage;
