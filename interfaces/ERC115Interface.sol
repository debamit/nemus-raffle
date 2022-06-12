// SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.9;
interface ERC115Interface {
    function balanceOfBatch(address[] calldata owners, uint256[] calldata ids) external view returns (uint256[] memory balances);
}
