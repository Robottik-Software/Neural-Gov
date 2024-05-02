
<p  align="center">

<a  href=""  rel="noopener">

<h3 align="center"><img width=200px  height=200px  src="https://robottik.com//resources/images/logo.png"  alt="Project logo"></a></h3>

</p>

  

<h3 align="center">Neural Gov</h3>
<h5 align="center" underline=none text-decoration=none>
A 
<a href="https://robottik.co.uk/" style="color: black; text-decoration: underline;text-decoration-style: dotted;">Robottik Software</a> Product</h5> 


  

<div align="center">

  

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Robottik-Software/Neural-Gov)](https://github.com/Robottik-Software/Neural-Gov/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Robottik-Software/Neural-Gov)](https://github.com/Robottik-Software/Neural-Gov/pulls)
[![License](https://img.shields.io/badge/license-GNU-blue.svg)](/LICENSE)
</div>

---

  

<p  align="center"> Open source, research orientated, practical application of Neural Networks within a government framework. Facilitating a range of interaction interfaces for demonstrative purposes.
<br>
Robottik Software is committed to developing powerful and influential technologies and research products.

<br>

We aren't ready yet. Star this repository to stay engaged in the process.

</p>

## 📝 Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Built By](#built_by)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)

## ℹ️ About <a name = "about"></a>

A research project run by Robottik Software, to identify the feasability of Neural Network implementation within a government framework.


## ⛏️ Build Level Design

Neural-Gov framework is detailed below for better execution and understanding of the assessment network which is a conglomeration of networks that make use of multiple hidden layers to provide a more accurate output result. Some of these input layers for each network are not necessarily input as data points which can be understood by the network, rather as textual content. Therefore before assessing the nodes against a network, we pass the nodes to a functionality known as pre-processing. It is here that the input data is converted to a numerical format for the usage of the network.

### Networks

#### General Network
- Receives a score, from underlying networks, for all attributes of a proposition. E.g. (Social Impact, Environmental Impact, Financial Impact, Political Impact)

#### Sentiment Analysis Network
- Determines the sentiment of a set of nodes. E.g. (Positive, Negative, Unchanging)
- Receives these nodes directly from the Textual Analysis Network

#### Textual Analysis Network
- Provided with phrases, from the Phrase Analysis Network, to assemble a boolean logical representation of particular phrases within the Proposition.

#### Phrase Analysis Network
- Provided with the entire proposition via the mainloop, the Phrase Analysis Network works to identify phrases within the proposition. E.g. the network would acquire: ```"more diverse workforce"``` from the proposition: ```"Implement a more diverse workforce by lowering the qualification requirements"```

#### Tokenisation Network
- Receives the proposition in string format and tokenises the entire string into individual characters, then returns it back into a list of words and punctuation.

## 🏁 Getting Started <a name = "getting_started"></a>

Not Yet Applicable.
Contact Robottik Software for more information/help/investment into research projects.

### Prerequisites

Not Yet Applicable.

### Installing

Not Yet Applicable.


## ⛏️ Built By <a name = "built_by"></a>

- [Robottik Software](https://robottik.com/) - Developer

## ✍️ Authors <a name = "authors"></a>

- [@romulushill](https://github.com/romulushill) - Founder & Lead
- R&D At Robottik Software

See also the list of [contributors](https://github.com/Robottik-Software/Neural-Gov/contributors) who participated in this project.
